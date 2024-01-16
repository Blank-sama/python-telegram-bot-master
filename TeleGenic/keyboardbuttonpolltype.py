"""This module contains an object that represents a type of a TeleGenic Poll."""
from typing import Any

from TeleGenic import TeleGenicObject


class KeyboardButtonPollType(TeleGenicObject):
    """This object represents type of a poll, which is allowed to be created
    and sent when the corresponding button is pressed.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`type` is equal.

    Attributes:
        type (:obj:`str`): Optional. If :attr:`TeleGenic.Poll.QUIZ` is passed, the user will be
            allowed to create only polls in the quiz mode. If :attr:`TeleGenic.Poll.REGULAR` is
            passed, only regular polls will be allowed. Otherwise, the user will be allowed to
            create a poll of any type.
    """

    __slots__ = ('type', '_id_attrs')

    def __init__(self, type: str = None, **_kwargs: Any):  # pylint: disable=W0622
        self.type = type

        self._id_attrs = (self.type,)
