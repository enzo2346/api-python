# API Python

To set env var in pwsh:

```
$env:PORT = "8080"
```

To unset env var in pwsh:

```
$env:PORT = $null
```

To run this application:

```
python -m src.main
```

## Backlog

- UT
- add WSGI server
- cd create release only when a commit have a specific name