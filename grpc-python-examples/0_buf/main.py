from proto.gen.pokeapi.v1 import pokedex_pb2

# class DummyPokemon:
#     def __init__(self, name="Pikachu", type="Electric", hp=35):
#         self.name = name
#         self.type = type
#         self.hp = hp
#
#     def __str__(self):
#         return f"Pokemon(name={self.name}, type={self.type}, hp={self.hp})"
#
#     def __repr__(self):
#         return self.__str__()

def main():
    # Simulate received request
    request = pokedex_pb2.GetPokemonRequest(name="Pikachu")
    print("Received request:")
    print(request)

    # # Simulate external pokemon.v1.Pokemon (which would normally be imported)
    # pikachu_proto = DummyPokemon(name="Pikachu", type="Electric", hp=35)
    #
    # # Simulate wrapping it into your own Pokemon message
    # wrapped = pokedex_pb2.Pokemon()
    # wrapped.pokemon.CopyFrom(pikachu_proto)  # Fails if DummyPokemon not actually a proto
    #
    # response = pokedex_pb2.GetPokemonResponse(pokemon=wrapped)
    # print("\nResponse:")
    # print(response)

if __name__ == "__main__":
    main()
