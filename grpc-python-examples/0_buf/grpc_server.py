import grpc
from concurrent import futures
import time

from proto.gen.pokeapi.v1 import pokedex_pb2, pokedex_pb2_grpc
from proto.gen.pokemon.v1 import types_pb2


class PokedexService(pokedex_pb2_grpc.PokedexServiceServicer):
    def GetPokemon(self, request, context):
        print(f"[SERVER] Received request for: {request.name}")

        pikachu = types_pb2.Pokemon(
            name="Pikachu",
            type=types_pb2.POKEMON_TYPE_ELECTRIC,
            abilities=[
                types_pb2.PokemonAbility(name="Static", description="May paralyze on contact.")
            ],
            moves=[
                types_pb2.PokemonMove(name="Thunderbolt", type=types_pb2.POKEMON_TYPE_ELECTRIC, power=90, accuracy=100)
            ],
            base_stats=types_pb2.PokemonStats(
                hp=35, attack=55, defense=40, special_attack=50, special_defense=50, speed=90
            )
        )

        return pokedex_pb2.GetPokemonResponse(
            pokemon=pokedex_pb2.Pokemon(pokemon=pikachu)
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pokedex_pb2_grpc.add_PokedexServiceServicer_to_server(PokedexService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("[SERVER] gRPC server is running on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
