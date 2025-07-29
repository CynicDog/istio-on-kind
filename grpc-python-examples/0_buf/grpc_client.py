import grpc
from proto.gen.pokeapi.v1 import pokedex_pb2, pokedex_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pokedex_pb2_grpc.PokedexServiceStub(channel)
        request = pokedex_pb2.GetPokemonRequest(name="Pikachu")
        response = stub.GetPokemon(request)
        print("[CLIENT] Got response:\n", response)

if __name__ == '__main__':
    run()
