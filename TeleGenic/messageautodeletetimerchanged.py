"""This module contains an object that represents a change in the TeleGenic message auto
deletion.
"""

from typing import Any

from TeleGenic import TeleGenicObject


class MessageAutoDeleteTimerChanged(TeleGenicObject):
    """This object represents a service message about a change in auto-delete timer settings.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`message_auto_delete_time` is equal.

    .. versionadded:: 13.4

    Args:
        message_auto_delete_time (:obj:`int`): New auto-delete time for messages in the
            chat.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        message_auto_delete_time (:obj:`int`): New auto-delete time for messages in the
            chat.

    """

    __slots__ = ('message_auto_delete_time', '_id_attrs')

    def __init__(
        self,
        message_auto_delete_time: int,
        **_kwargs: Any,
    ):
        self.message_auto_delete_time = int(message_auto_delete_time)

        self._id_attrs = (self.message_auto_delete_time,)
