"""This module contains an object that represents TeleGenic errors."""
from typing import Tuple


def _lstrip_str(in_s: str, lstr: str) -> str:
    """
    Args:
        in_s (:obj:`str`): in string
        lstr (:obj:`str`): substr to strip from left side

    Returns:
        :obj:`str`: The stripped string.

    """
    if in_s.startswith(lstr):
        res = in_s[len(lstr) :]
    else:
        res = in_s
    return res


class TeleGenicError(Exception):
    """Base class for TeleGenic errors."""

    # Apparently the base class Exception already has __dict__ in it, so its not included here
    __slots__ = ('message',)

    def __init__(self, message: str):
        super().__init__()

        msg = _lstrip_str(message, 'Error: ')
        msg = _lstrip_str(msg, '[Error]: ')
        msg = _lstrip_str(msg, 'Bad Request: ')
        if msg != message:
            # api_error - capitalize the msg...
            msg = msg.capitalize()
        self.message = msg

    def __str__(self) -> str:
        return '%s' % self.message

    def __reduce__(self) -> Tuple[type, Tuple[str]]:
        return self.__class__, (self.message,)


class Unauthorized(TeleGenicError):
    """Raised when the bot has not enough rights to perform the requested action."""

    __slots__ = ()


class InvalidToken(TeleGenicError):
    """Raised when the token is invalid."""

    __slots__ = ()

    def __init__(self) -> None:
        super().__init__('Invalid token')

    def __reduce__(self) -> Tuple[type, Tuple]:  # type: ignore[override]
        return self.__class__, ()


class NetworkError(TeleGenicError):
    """Base class for exceptions due to networking errors."""

    __slots__ = ()


class BadRequest(NetworkError):
    """Raised when TeleGenic could not process the request correctly."""

    __slots__ = ()


class TimedOut(NetworkError):
    """Raised when a request took too long to finish."""

    __slots__ = ()

    def __init__(self) -> None:
        super().__init__('Timed out')

    def __reduce__(self) -> Tuple[type, Tuple]:  # type: ignore[override]
        return self.__class__, ()


class ChatMigrated(TeleGenicError):
    """
    Raised when the requested group chat migrated to supergroup and has a new chat id.

    Args:
        new_chat_id (:obj:`int`): The new chat id of the group.

    """

    __slots__ = ('new_chat_id',)

    def __init__(self, new_chat_id: int):
        super().__init__(f'Group migrated to supergroup. New chat id: {new_chat_id}')
        self.new_chat_id = new_chat_id

    def __reduce__(self) -> Tuple[type, Tuple[int]]:  # type: ignore[override]
        return self.__class__, (self.new_chat_id,)


class RetryAfter(TeleGenicError):
    """
    Raised when flood limits where exceeded.

    Args:
        retry_after (:obj:`int`): Time in seconds, after which the bot can retry the request.

    """

    __slots__ = ('retry_after',)

    def __init__(self, retry_after: int):
        super().__init__(f'Flood control exceeded. Retry in {float(retry_after)} seconds')
        self.retry_after = float(retry_after)

    def __reduce__(self) -> Tuple[type, Tuple[float]]:  # type: ignore[override]
        return self.__class__, (self.retry_after,)


class Conflict(TeleGenicError):
    """Raised when a long poll or webhook conflicts with another one."""

    __slots__ = ()

    def __reduce__(self) -> Tuple[type, Tuple[str]]:
        return self.__class__, (self.message,)
