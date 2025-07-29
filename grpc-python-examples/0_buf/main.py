from proto.gen.pokeapi.v1 import pokedex_pb2
from proto.gen.pokemon.v1 import types_pb2

def main():
    # Simulate a request
    request = pokedex_pb2.GetPokemonRequest(name="Pikachu")
    print("Received request:")
    print(request)

    # Create Pikachu abilities
    static_ability = types_pb2.PokemonAbility(
        name="Static",
        description="May cause paralysis on contact."
    )

    lightning_rod_ability = types_pb2.PokemonAbility(
        name="Lightning Rod",
        description="Draws in all Electric-type moves."
    )

    # Create Pikachu moves
    thunderbolt = types_pb2.PokemonMove(
        name="Thunderbolt",
        type=types_pb2.POKEMON_TYPE_ELECTRIC,
        power=90,
        accuracy=100
    )

    quick_attack = types_pb2.PokemonMove(
        name="Quick Attack",
        type=types_pb2.POKEMON_TYPE_NORMAL,
        power=40,
        accuracy=100
    )

    # Base stats
    stats = types_pb2.PokemonStats(
        hp=35,
        attack=55,
        defense=40,
        special_attack=50,
        special_defense=50,
        speed=90
    )

    # The full Pikachu message
    pikachu_proto = types_pb2.Pokemon(
        name="Pikachu",
        type=types_pb2.POKEMON_TYPE_ELECTRIC,
        abilities=[static_ability, lightning_rod_ability],
        moves=[thunderbolt, quick_attack],
        base_stats=stats
    )

    # Wrap in PokedexService response
    wrapped = pokedex_pb2.Pokemon(pokemon=pikachu_proto)
    response = pokedex_pb2.GetPokemonResponse(pokemon=wrapped)

    print("\nResponse:")
    print(response)

if __name__ == "__main__":
    main()
