# 1_route_guide

## Overview

This project demonstrates how to use gRPC with Protocol Buffers in Python using the `uv` tool for environment and dependency management.

## Getting Started

### 1. Initialize your project

Run the following command to create a new `uv` project called `1_route_guide`:

```bash
uv init 1_route_guide
```

### 2. Add gRPC dependencies and activate the virtual environment

Install the required gRPC tools and libraries, and activate the created virtual environment:

```bash
uv add grpcio-tools
source .venv/bin/activate
```

* `uv add grpcio-tools` installs `grpcio`, `grpcio-tools`, and their dependencies into the `.venv` virtual environment.
* `source .venv/bin/activate` activates the virtual environment so your shell uses the correct Python interpreter and packages.

### 3. Compile the Protocol Buffers `.proto` file

Generate Python code from your `route_guide.proto` file:

```bash
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. route_guide.proto
```
> * `-I.` tells `protoc` to look for imports relative to the current directory.
> * `--python_out=.` generates the base Python classes for your protobuf messages.
> * `--pyi_out=.` generates type stub files (`.pyi`) to help with type checking in editors.
> * `--grpc_python_out=.` generates gRPC-specific code for client and server stubs.

or 
```bash 
uv run run_codegen.py 
```

### 4. Run the server and client 
Run the server:
```bash
uv run route_guide_server.py
```

From a different terminal, run the client:
```bash
uv run route_guide_client.py
```
