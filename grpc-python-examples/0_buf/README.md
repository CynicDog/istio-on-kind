## Run `main.py` script 
Tell Python to treat `proto/gen` as the root of the import tree:

```bash
PYTHONPATH=proto/gen uv run main.py  # on macOS/Linux
```

On **Windows**, in PowerShell:

```powershell
$env:PYTHONPATH = "proto/gen"
uv run main.py
```

## Run grpc Server and Client 

### Terminal 1 — Start server:

```bash
$env:PYTHONPATH = "proto/gen"       # PowerShell (Windows)
uv run server.py
```

Or on Unix/macOS:

```bash
PYTHONPATH=proto/gen uv run server.py
```

### Terminal 2 — Run client:

```bash
$env:PYTHONPATH = "proto/gen"
uv run client.py
```

Or on Unix/macOS:

```bash
PYTHONPATH=proto/gen uv run client.py
```