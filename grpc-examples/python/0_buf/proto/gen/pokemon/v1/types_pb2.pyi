from buf.validate import validate_pb2 as _validate_pb2
from google.type import datetime_pb2 as _datetime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PokemonType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POKEMON_TYPE_UNSPECIFIED: _ClassVar[PokemonType]
    POKEMON_TYPE_NORMAL: _ClassVar[PokemonType]
    POKEMON_TYPE_FIRE: _ClassVar[PokemonType]
    POKEMON_TYPE_WATER: _ClassVar[PokemonType]
    POKEMON_TYPE_ELECTRIC: _ClassVar[PokemonType]
    POKEMON_TYPE_GRASS: _ClassVar[PokemonType]
    POKEMON_TYPE_ICE: _ClassVar[PokemonType]
    POKEMON_TYPE_FIGHTING: _ClassVar[PokemonType]
    POKEMON_TYPE_POISON: _ClassVar[PokemonType]
    POKEMON_TYPE_GROUND: _ClassVar[PokemonType]
    POKEMON_TYPE_FLYING: _ClassVar[PokemonType]
    POKEMON_TYPE_PSYCHIC: _ClassVar[PokemonType]
    POKEMON_TYPE_BUG: _ClassVar[PokemonType]
    POKEMON_TYPE_ROCK: _ClassVar[PokemonType]
    POKEMON_TYPE_GHOST: _ClassVar[PokemonType]
    POKEMON_TYPE_DARK: _ClassVar[PokemonType]
    POKEMON_TYPE_STEEL: _ClassVar[PokemonType]
    POKEMON_TYPE_FAIRY: _ClassVar[PokemonType]

class BattleStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BATTLE_STATUS_UNSPECIFIED: _ClassVar[BattleStatus]
    BATTLE_STATUS_ONGOING: _ClassVar[BattleStatus]
    BATTLE_STATUS_WON_BY_TRAINER1: _ClassVar[BattleStatus]
    BATTLE_STATUS_WON_BY_TRAINER2: _ClassVar[BattleStatus]
    BATTLE_STATUS_DRAW: _ClassVar[BattleStatus]
POKEMON_TYPE_UNSPECIFIED: PokemonType
POKEMON_TYPE_NORMAL: PokemonType
POKEMON_TYPE_FIRE: PokemonType
POKEMON_TYPE_WATER: PokemonType
POKEMON_TYPE_ELECTRIC: PokemonType
POKEMON_TYPE_GRASS: PokemonType
POKEMON_TYPE_ICE: PokemonType
POKEMON_TYPE_FIGHTING: PokemonType
POKEMON_TYPE_POISON: PokemonType
POKEMON_TYPE_GROUND: PokemonType
POKEMON_TYPE_FLYING: PokemonType
POKEMON_TYPE_PSYCHIC: PokemonType
POKEMON_TYPE_BUG: PokemonType
POKEMON_TYPE_ROCK: PokemonType
POKEMON_TYPE_GHOST: PokemonType
POKEMON_TYPE_DARK: PokemonType
POKEMON_TYPE_STEEL: PokemonType
POKEMON_TYPE_FAIRY: PokemonType
BATTLE_STATUS_UNSPECIFIED: BattleStatus
BATTLE_STATUS_ONGOING: BattleStatus
BATTLE_STATUS_WON_BY_TRAINER1: BattleStatus
BATTLE_STATUS_WON_BY_TRAINER2: BattleStatus
BATTLE_STATUS_DRAW: BattleStatus

class Pokemon(_message.Message):
    __slots__ = ("name", "type", "abilities", "moves", "base_stats")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ABILITIES_FIELD_NUMBER: _ClassVar[int]
    MOVES_FIELD_NUMBER: _ClassVar[int]
    BASE_STATS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: PokemonType
    abilities: _containers.RepeatedCompositeFieldContainer[PokemonAbility]
    moves: _containers.RepeatedCompositeFieldContainer[PokemonMove]
    base_stats: PokemonStats
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[PokemonType, str]] = ..., abilities: _Optional[_Iterable[_Union[PokemonAbility, _Mapping]]] = ..., moves: _Optional[_Iterable[_Union[PokemonMove, _Mapping]]] = ..., base_stats: _Optional[_Union[PokemonStats, _Mapping]] = ...) -> None: ...

class PokemonAbility(_message.Message):
    __slots__ = ("name", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class PokemonMove(_message.Message):
    __slots__ = ("name", "type", "power", "accuracy")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    ACCURACY_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: PokemonType
    power: int
    accuracy: int
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[PokemonType, str]] = ..., power: _Optional[int] = ..., accuracy: _Optional[int] = ...) -> None: ...

class PokemonStats(_message.Message):
    __slots__ = ("hp", "attack", "defense", "special_attack", "special_defense", "speed")
    HP_FIELD_NUMBER: _ClassVar[int]
    ATTACK_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_ATTACK_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_DEFENSE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int
    def __init__(self, hp: _Optional[int] = ..., attack: _Optional[int] = ..., defense: _Optional[int] = ..., special_attack: _Optional[int] = ..., special_defense: _Optional[int] = ..., speed: _Optional[int] = ...) -> None: ...

class Trainer(_message.Message):
    __slots__ = ("name", "pokemon_team")
    NAME_FIELD_NUMBER: _ClassVar[int]
    POKEMON_TEAM_FIELD_NUMBER: _ClassVar[int]
    name: str
    pokemon_team: _containers.RepeatedCompositeFieldContainer[Pokemon]
    def __init__(self, name: _Optional[str] = ..., pokemon_team: _Optional[_Iterable[_Union[Pokemon, _Mapping]]] = ...) -> None: ...

class PokedexEntry(_message.Message):
    __slots__ = ("number", "species", "description", "primary_type", "secondary_type", "possible_abilities")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    SPECIES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_TYPE_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_ABILITIES_FIELD_NUMBER: _ClassVar[int]
    number: int
    species: str
    description: str
    primary_type: PokemonType
    secondary_type: PokemonType
    possible_abilities: _containers.RepeatedCompositeFieldContainer[PokemonAbility]
    def __init__(self, number: _Optional[int] = ..., species: _Optional[str] = ..., description: _Optional[str] = ..., primary_type: _Optional[_Union[PokemonType, str]] = ..., secondary_type: _Optional[_Union[PokemonType, str]] = ..., possible_abilities: _Optional[_Iterable[_Union[PokemonAbility, _Mapping]]] = ...) -> None: ...

class Battle(_message.Message):
    __slots__ = ("trainer1", "trainer2", "active_pokemon_trainer1", "active_pokemon_trainer2", "turn_number", "status", "actions", "start_time")
    TRAINER1_FIELD_NUMBER: _ClassVar[int]
    TRAINER2_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_POKEMON_TRAINER1_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_POKEMON_TRAINER2_FIELD_NUMBER: _ClassVar[int]
    TURN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    trainer1: Trainer
    trainer2: Trainer
    active_pokemon_trainer1: _containers.RepeatedCompositeFieldContainer[Pokemon]
    active_pokemon_trainer2: _containers.RepeatedCompositeFieldContainer[Pokemon]
    turn_number: int
    status: BattleStatus
    actions: _containers.RepeatedCompositeFieldContainer[BattleAction]
    start_time: _datetime_pb2.DateTime
    def __init__(self, trainer1: _Optional[_Union[Trainer, _Mapping]] = ..., trainer2: _Optional[_Union[Trainer, _Mapping]] = ..., active_pokemon_trainer1: _Optional[_Iterable[_Union[Pokemon, _Mapping]]] = ..., active_pokemon_trainer2: _Optional[_Iterable[_Union[Pokemon, _Mapping]]] = ..., turn_number: _Optional[int] = ..., status: _Optional[_Union[BattleStatus, str]] = ..., actions: _Optional[_Iterable[_Union[BattleAction, _Mapping]]] = ..., start_time: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]] = ...) -> None: ...

class BattleAction(_message.Message):
    __slots__ = ("turn", "action_text")
    TURN_FIELD_NUMBER: _ClassVar[int]
    ACTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    turn: int
    action_text: str
    def __init__(self, turn: _Optional[int] = ..., action_text: _Optional[str] = ...) -> None: ...
