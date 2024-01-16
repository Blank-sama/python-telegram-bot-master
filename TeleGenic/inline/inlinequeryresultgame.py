"""This module contains the classes that represent TeleGenic InlineQueryResultGame."""

from typing import TYPE_CHECKING, Any

from TeleGenic import InlineQueryResult

if TYPE_CHECKING:
    from TeleGenic import ReplyMarkup


class InlineQueryResultGame(InlineQueryResult):
    """Represents a :class:`TeleGenic.Game`.

    Args:
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        game_short_name (:obj:`str`): Short name of the game.
        reply_markup (:class:`TeleGenic.InlineKeyboardMarkup`, optional): Inline keyboard attached
            to the message.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        type (:obj:`str`): 'game'.
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        game_short_name (:obj:`str`): Short name of the game.
        reply_markup (:class:`TeleGenic.InlineKeyboardMarkup`): Optional. Inline keyboard attached
            to the message.

    """

    __slots__ = ('reply_markup', 'game_short_name')

    def __init__(
        self,
        id: str,  # pylint: disable=W0622
        game_short_name: str,
        reply_markup: 'ReplyMarkup' = None,
        **_kwargs: Any,
    ):
        # Required
        super().__init__('game', id)
        self.id = id  # pylint: disable=W0622
        self.game_short_name = game_short_name

        self.reply_markup = reply_markup
