"""This module contains custom typing aliases.

.. versionadded:: 13.6
"""
from typing import TypeVar, TYPE_CHECKING, Tuple, List, Dict, Any, Optional

if TYPE_CHECKING:
    from TeleGenic.ext import CallbackContext  # noqa: F401


ConversationDict = Dict[Tuple[int, ...], Optional[object]]
"""Dicts as maintained by the :class:`telegram.ext.ConversationHandler`.

    .. versionadded:: 13.6
"""

CDCData = Tuple[List[Tuple[str, float, Dict[str, Any]]], Dict[str, str]]
"""Tuple[List[Tuple[:obj:`str`, :obj:`float`, Dict[:obj:`str`, :obj:`any`]]], \
    Dict[:obj:`str`, :obj:`str`]]: Data returned by
    :attr:`telegram.ext.CallbackDataCache.persistence_data`.

    .. versionadded:: 13.6
"""

CCT = TypeVar('CCT', bound='CallbackContext')
"""An instance of :class:`telegram.ext.CallbackContext` or a custom subclass.

.. versionadded:: 13.6
"""
UD = TypeVar('UD')
"""Type of the user data for a single user.

.. versionadded:: 13.6
"""
CD = TypeVar('CD')
"""Type of the chat data for a single user.

.. versionadded:: 13.6
"""
BD = TypeVar('BD')
"""Type of the bot data.

.. versionadded:: 13.6
"""
