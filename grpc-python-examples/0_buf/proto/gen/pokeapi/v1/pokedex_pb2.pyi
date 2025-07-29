from pokemon.v1 import types_pb2 as _types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetPokemonRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetPokemonResponse(_message.Message):
    __slots__ = ("pokemon",)
    POKEMON_FIELD_NUMBER: _ClassVar[int]
    pokemon: Pokemon
    def __init__(self, pokemon: _Optional[_Union[Pokemon, _Mapping]] = ...) -> None: ...

class Pokemon(_message.Message):
    __slots__ = ("pokemon",)
    POKEMON_FIELD_NUMBER: _ClassVar[int]
    pokemon: _types_pb2.Pokemon
    def __init__(self, pokemon: _Optional[_Union[_types_pb2.Pokemon, _Mapping]] = ...) -> None: ...
