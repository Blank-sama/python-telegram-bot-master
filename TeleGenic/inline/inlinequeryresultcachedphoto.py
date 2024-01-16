"""This module contains the classes that represent TeleGenic InlineQueryResultPhoto"""

from typing import TYPE_CHECKING, Any, Union, Tuple, List

from TeleGenic import InlineQueryResult, MessageEntity
from TeleGenic.utils.helpers import DEFAULT_NONE
from TeleGenic.utils.types import ODVInput

if TYPE_CHECKING:
    from TeleGenic import InputMessageContent, ReplyMarkup


class InlineQueryResultCachedPhoto(InlineQueryResult):
    """
    Represents a link to a photo stored on the TeleGenic servers. By default, this photo will be
    sent by the user with an optional caption. Alternatively, you can use
    :attr:`input_message_content` to send a message with the specified content instead
    of the photo.

    Args:
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        photo_file_id (:obj:`str`): A valid file identifier of the photo.
        title (:obj:`str`, optional): Title for the result.
        description (:obj:`str`, optional): Short description of the result.
        caption (:obj:`str`, optional): Caption of the photo to be sent, 0-1024 characters after
            entities parsing.
        parse_mode (:obj:`str`, optional): Send Markdown or HTML, if you want TeleGenic apps to show
            bold, italic, fixed-width text or inline URLs in the media caption. See the constants
            in :class:`TeleGenic.ParseMode` for the available modes.
        caption_entities (List[:class:`TeleGenic.MessageEntity`], optional): List of special
            entities that appear in the caption, which can be specified instead of
            :attr:`parse_mode`.
        reply_markup (:class:`TeleGenic.InlineKeyboardMarkup`, optional): Inline keyboard attached
            to the message.
        input_message_content (:class:`TeleGenic.InputMessageContent`, optional): Content of the
            message to be sent instead of the photo.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        type (:obj:`str`): 'photo'.
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        photo_file_id (:obj:`str`): A valid file identifier of the photo.
        title (:obj:`str`): Optional. Title for the result.
        description (:obj:`str`): Optional. Short description of the result.
        caption (:obj:`str`): Optional. Caption of the photo to be sent, 0-1024 characters after
            entities parsing.
        parse_mode (:obj:`str`): Optional. Send Markdown or HTML, if you want TeleGenic apps to show
            bold, italic, fixed-width text or inline URLs in the media caption. See the constants
            in :class:`TeleGenic.ParseMode` for the available modes.
        caption_entities (List[:class:`TeleGenic.MessageEntity`]): Optional. List of special
            entities that appear in the caption, which can be specified instead of
            :attr:`parse_mode`.
        reply_markup (:class:`TeleGenic.InlineKeyboardMarkup`): Optional. Inline keyboard attached
            to the message.
        input_message_content (:class:`TeleGenic.InputMessageContent`): Optional. Content of the
            message to be sent instead of the photo.

    """

    __slots__ = (
        'reply_markup',
        'caption_entities',
        'caption',
        'title',
        'description',
        'parse_mode',
        'photo_file_id',
        'input_message_content',
    )

    def __init__(
        self,
        id: str,  # pylint: disable=W0622
        photo_file_id: str,
        title: str = None,
        description: str = None,
        caption: str = None,
        reply_markup: 'ReplyMarkup' = None,
        input_message_content: 'InputMessageContent' = None,
        parse_mode: ODVInput[str] = DEFAULT_NONE,
        caption_entities: Union[Tuple[MessageEntity, ...], List[MessageEntity]] = None,
        **_kwargs: Any,
    ):
        # Required
        super().__init__('photo', id)
        self.photo_file_id = photo_file_id

        # Optionals
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
