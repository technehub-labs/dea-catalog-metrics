# Shard `g`

CR-MET-024 bucket for record slugs starting with `g`. The shard
key is the first character of the id's slug (the id minus the
`dea:metric-` prefix); digit-leading slugs live in `0-9/`. The path
stays derivable from the id alone (entity-storage-layout.md §5):
`entities/v1-alpha/<shard>/<dea:metric-...>/<dea:metric-...>.yaml`.
