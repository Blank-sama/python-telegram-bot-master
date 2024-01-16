"""This module contains an object that represents a TeleGenic ReplyKeyboardRemove."""
from typing import Any

from TeleGenic import ReplyMarkup


class ReplyKeyboardRemove(ReplyMarkup):
    """
    Upon receiving a message with this object, TeleGenic clients will remove the current custom
    keyboard and display the default letter-keyboard. By default, custom keyboards are displayed
    until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are
    hidden immediately after the user presses a button (see :class:`TeleGenic.ReplyKeyboardMarkup`).

    Example:
        A user votes in a poll, bot returns confirmation message in reply to the vote and removes
        the keyboard for that user, while still showing the keyboard with poll options to users who
        haven't voted yet.

    Note:
        User will not be able to summon this keyboard; if you want to hide the keyboard from
        sight but keep it accessible, use :attr:`TeleGenic.ReplyKeyboardMarkup.one_time_keyboard`.

    Args:
        selective (:obj:`bool`, optional): Use this parameter if you want to remove the keyboard
            for specific users only. Targets:

            1) Users that are @mentioned in the text of the :class:`TeleGenic.Message` object.
            2) If the bot's message is a reply (has `reply_to_message_id`), sender of the original
               message.

        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        remove_keyboard (:obj:`True`): Requests clients to remove the custom keyboard.
        selective (:obj:`bool`): Optional. Use this parameter if you want to remove the keyboard
            for specific users only.

    """

    __slots__ = ('selective', 'remove_keyboard')

    def __init__(self, selective: bool = False, **_kwargs: Any):
        # Required
        self.remove_keyboard = True
        # Optionals
        self.selective = bool(selective)
