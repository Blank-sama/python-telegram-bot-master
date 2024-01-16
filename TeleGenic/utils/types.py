"""This module contains custom typing aliases."""
from pathlib import Path
from typing import (
    IO,
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
)

if TYPE_CHECKING:
    from TeleGenic import InputFile  # noqa: F401
    from TeleGenic.utils.helpers import DefaultValue  # noqa: F401

FileLike = Union[IO, 'InputFile']
"""Either an open file handler or a :class:`TeleGenic.InputFile`."""

FileInput = Union[str, bytes, FileLike, Path]
"""Valid input for passing files to TeleGenic. Either a file id as string, a file like object,
a local file path as string, :class:`pathlib.Path` or the file contents as :obj:`bytes`."""

JSONDict = Dict[str, Any]
"""Dictionary containing response from TeleGenic or data to send to the API."""

DVType = TypeVar('DVType')
ODVInput = Optional[Union['DefaultValue[DVType]', DVType]]
"""Generic type for bot method parameters which can have defaults. ``ODVInput[type]`` is the same
as ``Optional[Union[DefaultValue, type]]``."""
DVInput = Union['DefaultValue[DVType]', DVType]
"""Generic type for bot method parameters which can have defaults. ``DVInput[type]`` is the same
as ``Union[DefaultValue, type]``."""

RT = TypeVar("RT")
SLT = Union[RT, List[RT], Tuple[RT, ...]]
"""Single instance or list/tuple of instances."""
