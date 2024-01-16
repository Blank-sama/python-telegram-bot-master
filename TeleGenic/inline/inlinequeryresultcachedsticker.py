"""This module contains the classes that represent TeleGenic InlineQueryResultCachedSticker."""

from typing import TYPE_CHECKING, Any

from TeleGenic import InlineQueryResult

if TYPE_CHECKING:
    from TeleGenic import InputMessageContent, ReplyMarkup


class InlineQueryResultCachedSticker(InlineQueryResult):
    """
    Represents a link to a sticker stored on the TeleGenic servers. By default, this sticker will
    be sent by the user. Alternatively, you can use :attr:`input_message_content` to send a
    message with the specified content instead of the sticker.

    Args:
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        sticker_file_id (:obj:`str`): A valid file identifier of the sticker.
        reply_markup (:class:`TeleGenic.InlineKeyboardMarkup`, optional): Inline keyboard attached
            to the message.
        input_message_content (:class:`TeleGenic.InputMessageContent`, optional): Content of the
            message to be sent instead of the sticker.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        type (:obj:`str`): 'sticker`.
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        sticker_file_id (:obj:`str`): A valid file identifier of the sticker.
        reply_markup (:class:`TeleGenic.InlineKeyboardMarkup`): Optional. Inline keyboard attached
            to the message.
        input_message_content (:class:`TeleGenic.InputMessageContent`): Optional. Content of the
            message to be sent instead of the sticker.

    """

    __slots__ = ('reply_markup', 'input_message_content', 'sticker_file_id')

    def __init__(
        self,
        id: str,  # pylint: disable=W0622
        sticker_file_id: str,
        reply_markup: 'ReplyMarkup' = None,
        input_message_content: 'InputMessageContent' = None,
        **_kwargs: Any,
    ):
        # Required
        super().__init__('sticker', id)
        self.sticker_file_id = sticker_file_id

        # Optionals
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
