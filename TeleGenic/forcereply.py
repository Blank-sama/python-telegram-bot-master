"""This module contains an object that represents a TeleGenic ForceReply."""

from typing import Any

from TeleGenic import ReplyMarkup


class ForceReply(ReplyMarkup):
    """
    Upon receiving a message with this object, TeleGenic clients will display a reply interface to
    the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be
    extremely useful if you want to create user-friendly step-by-step interfaces without having
    to sacrifice privacy mode.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`selective` is equal.

    Args:
        selective (:obj:`bool`, optional): Use this parameter if you want to force reply from
            specific users only. Targets:

            1) Users that are @mentioned in the :attr:`~TeleGenic.Message.text` of the
               :class:`TeleGenic.Message` object.
            2) If the bot's message is a reply (has ``reply_to_message_id``), sender of the
               original message.

        input_field_placeholder (:obj:`str`, optional): The placeholder to be shown in the input
            field when the reply is active; 1-64 characters.

            .. versionadded:: 13.7

        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        force_reply (:obj:`True`): Shows reply interface to the user, as if they manually selected
            the bots message and tapped 'Reply'.
        selective (:obj:`bool`): Optional. Force reply from specific users only.
        input_field_placeholder (:obj:`str`): Optional. The placeholder shown in the input
            field when the reply is active.

            .. versionadded:: 13.7

    """

    __slots__ = ('selective', 'force_reply', 'input_field_placeholder', '_id_attrs')

    def __init__(
        self,
        force_reply: bool = True,
        selective: bool = False,
        input_field_placeholder: str = None,
        **_kwargs: Any,
    ):
        # Required
        self.force_reply = bool(force_reply)
        # Optionals
        self.selective = bool(selective)
        self.input_field_placeholder = input_field_placeholder

        self._id_attrs = (self.selective,)
