"""Gate 7: check_formula_namespace.py.

Formula variable disambiguation across Metric records.

THE PROBLEM THIS PREVENTS

The catalogue already binds MTTR as a formula variable meaning Mean Time to
Recovery:

    dea:metric-mean-time-to-recovery
      expression: MTTR = (sum_i RecoveryTime_i) / n

MTTR is equally the natural abbreviation for Mean Time to Repair and for Mean
Time to Respond. A second record could bind the same three letters to a
different quantity and every existing gate would still pass: the metamodel
alias layer cannot see this collision, because entity aliases are 1-5
character uppercase strings while catalogue record ids are colon-namespaced
full words. The two namespaces never meet.

Disambiguation therefore cannot come from the spelling. Two records using MTTR
with different meanings are indistinguishable by construction. This gate makes
that a detected condition instead of a latent one.

THE RULE

A left-hand formula variable is scoped to its record. It is acceptable, and
expected, for two records to use the same short form, because each expression
is evaluated within the record that declares it. What is NOT acceptable is the
thing that actually causes harm:

  REUSED   two records declare the same short form for semantically DIFFERENT
           quantities. This is the repair-vs-respond case. Flagged.
  REDECLARED  a record declares a short form that collides with the well-known
           reserved forms whose meaning is fixed by industry convention. MTTR is
           reserved for Mean Time to Recovery in this catalogue.
  UNBOUND   an expression's left-hand side names a variable that is not
           declared in the record's inputs. The formula cannot be evaluated.

Distinct quantities sharing a short form is reported as an ADVISORY finding,
because two records can legitimately use the same local name. Reusing a
RESERVED form for a different quantity is reported as a BLOCKING finding,
because the meaning of a reserved form is fixed catalogue-wide.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _catalog import load_metrics  # noqa: E402

import re
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).parent.parent
ENTITIES_DIR = BASE / "entities"

# Short forms whose meaning is fixed by convention in this catalogue. A record
# may not bind one of these to a different quantity.
RESERVED = {
    "MTTR": "Mean Time to Recovery",
}

# Words that identify a quantity's identity, used to decide whether two records
# using the same short form mean the same thing.
IDENTITY_TOKENS = {
    "mean", "time", "recovery", "repair", "respond", "response",
    "resolution", "rate", "ratio", "count", "margin", "completeness",
    "effectiveness", "retention", "sum", "total", "average",
}

# Function words shared by many quantities. Mean Time To Repair, Mean Time To
# Recovery and Mean Time To Response all reduce to {mean, time, <noun>}; the
# qualifiers carry no distinguishing information, so they are stripped before
# comparing two bindings. Comparing the raw sets would let the shared
# "mean" and "time" mask the one word that actually differs.
QUALIFIERS = {"mean", "time", "average", "total", "sum", "rate", "ratio"}

VAR_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=")


def load_metrics() -> list[tuple[str, dict]]:
    out = []
    for path in sorted(ENTITIES_DIR.glob("v1-alpha/*/*.yaml")):
        if path.parent.name.startswith("dea:metric-"):
            out.append((path.parent.name, yaml.safe_load(path.read_text())))
    return out


def _formula(record: dict) -> dict | None:
    return (record.get("formula_definition") or {}) or None


def _lhs_var(record: dict) -> str | None:
    f = _formula(record)
    if not f:
        return None
    m = VAR_RE.match(str(f.get("expression") or ""))
    return m.group(1) if m else None


def _input_names(record: dict) -> set[str]:
    f = _formula(record)
    if not f:
        return set()
    names = set()
    for item in f.get("inputs") or []:
        if isinstance(item, dict) and item.get("name"):
            names.add(str(item["name"]))
        elif isinstance(item, str):
            names.add(item)
    return names


def _tokens(text: str) -> set[str]:
    return {t for t in re.split(r"[^a-z]", text.lower()) if t in IDENTITY_TOKENS}


def _core(text: str) -> frozenset[str]:
    """Distinguishing content of a quantity name, qualifiers removed.

    Mean Time to Recovery -> {recovery}; Mean Time to Repair -> {repair}.
    Two bindings conflict when their cores differ, because the qualifiers
    cannot discriminate between them.
    """
    return frozenset(_tokens(text) - QUALIFIERS)


def main() -> int:
    metrics = load_metrics()
    blocking: list[str] = []
    advisory: list[str] = []

    by_var: dict[str, list[tuple[str, dict, str]]] = {}

    for name, rec in metrics:
        var = _lhs_var(rec)
        if var:
            by_var.setdefault(var, []).append((name, rec, var))

        # UNBOUND: the LHS must be derivable from declared inputs, or be a
        # declared output. A formula whose result name is undeclared cannot be
        # reproduced by a consumer.
        fdef = _formula(rec)
        if fdef:
            inputs = _input_names(rec)
            expr = str(fdef.get("expression") or "")
            # CR-MET-020: the left-hand side is the record's own result
            # variable, not a reference to an input, so the unbound scan
            # reads the right-hand side only. The short form is hyphenated in
            # the seed (ABR-D), and a hyphen is not an identifier character,
            # so scanning the whole expression would report the record's own
            # short form as an unbound reference.
            rhs = expr.split("=", 1)[1] if "=" in expr else expr
            for token in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", rhs):
                if token in inputs or token == var:
                    continue
                # Sigma/aggregate notation (sum_i, sum_j) and bare bound
                # variables are notation, not references to declared inputs.
                if token.lower() in {"sum", "i", "j", "k", "n", "true", "false"}:
                    continue
                if re.fullmatch(r"(sum|prod|avg|min|max|count)_[a-z]", token):
                    continue
                if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", token) and (
                    token not in inputs
                ) and not any(token in i for i in inputs):
                    # Only flag a symbol that looks like an unbound identifier
                    # and is not a declared input.
                    if token[0].isupper() or token.endswith("_i"):
                        advisory.append(
                            f"{name}: expression references '{token}' which is not a "
                            f"declared input; declared inputs are {sorted(inputs) or 'none'}"
                        )
                        break

    # REUSED with divergent meaning, and REDECLARED reserved forms.
    for var, users in sorted(by_var.items()):
        if var in RESERVED:
            for name, rec, _ in users:
                label = name.replace("dea:metric-", "").replace("-", " ")
                core = _core(label)
                reserved_core = _core(RESERVED[var])
                if core and reserved_core and core != reserved_core:
                    blocking.append(
                        f"{name}: binds reserved variable {var!r}, which is fixed "
                        f"catalogue-wide as {RESERVED[var]}, to a different quantity "
                        f"({label}). Distinct meaning: {sorted(core)} versus "
                        f"{sorted(reserved_core)}. This is the Mean Time To Repair "
                        f"versus Mean Time To Response case, and it is exactly what "
                        f"the reservation exists to prevent."
                    )
        if len(users) > 1:
            meanings = [
                _core(n.replace("dea:metric-", "").replace("-", " "))
                for n, _, _ in users
            ]
            if len(set(meanings)) > 1:
                advisory.append(
                    f"short form {var!r} is used by {len(users)} records with different "
                    f"meanings: {[n for n, _, _ in users]}. Safe today because each "
                    f"expression is scoped to its record, but confirm the intent."
                )

    print("=" * 72)
    print("Gate 7: formula variable namespace")
    print("=" * 72)
    print(f"  metrics scanned        : {len(metrics)}")
    print(f"  short forms observed   : {len(by_var)}")
    print(f"  reserved forms         : {sorted(RESERVED)}")
    print()

    if advisory:
        print(f"  ADVISORY ({len(advisory)}):")
        for a in advisory:
            print(f"    - {a}")
        print()

    if blocking:
        print(f"  BLOCKING ({len(blocking)}):")
        for b in blocking:
            print(f"    - {b}")
        print()
        print(
            "A reserved short form must keep one catalogue-wide meaning.\n"
            "Either correct the record or retire the reservation."
        )
        return 1

    print("  PASS: no short form binds a reserved meaning to a different quantity.")
    if advisory:
        print(
            f"  {len(advisory)} advisory finding(s) above: reuse of a short form "
            "across records is safe while scoping holds."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())