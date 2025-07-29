from grpc_tools import protoc

proto_include = "./proto"  # path to your proto root folder with envoy/, udpa/, etc.

proto_files = [
    "envoy/service/discovery/v3/ads.proto",
    "envoy/config/listener/v3/listener.proto",
    "envoy/config/route/v3/route.proto",
    "envoy/config/cluster/v3/cluster.proto",
    "envoy/config/endpoint/v3/endpoint.proto",
    # add more proto files as needed
]

protoc_args = [
    "",
    f"-I{proto_include}",
    "--python_out=.",
    "--grpc_python_out=.",
]

protoc_args.extend([f"{proto_include}/{pf}" for pf in proto_files])

if protoc.main(protoc_args) != 0:
    raise Exception("Error: protoc command failed")
