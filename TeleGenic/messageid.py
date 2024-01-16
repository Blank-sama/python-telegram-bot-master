"""This module contains an object that represents an instance of a TeleGenic MessageId."""
from typing import Any

from TeleGenic import TeleGenicObject


class MessageId(TeleGenicObject):
    """This object represents a unique message identifier.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`message_id` is equal.

    Attributes:
        message_id (:obj:`int`): Unique message identifier
    """

    __slots__ = ('message_id', '_id_attrs')

    def __init__(self, message_id: int, **_kwargs: Any):
        self.message_id = int(message_id)

        self._id_attrs = (self.message_id,)
