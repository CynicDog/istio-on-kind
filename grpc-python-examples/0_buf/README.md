### Set PYTHONPATH when running

Tell Python to treat `proto/gen` as the root of the import tree:

```bash
PYTHONPATH=proto/gen uv run main.py  # on macOS/Linux
```

On **Windows**, in PowerShell:

```powershell
$env:PYTHONPATH = "proto/gen"
uv run main.py
```