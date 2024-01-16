"""This module contains the classes that represent TeleGenic InlineQueryResultCachedVideo."""

from typing import TYPE_CHECKING, Any, Union, Tuple, List

from TeleGenic import InlineQueryResult, MessageEntity
from TeleGenic.utils.helpers import DEFAULT_NONE
from TeleGenic.utils.types import ODVInput

if TYPE_CHECKING:
    from TeleGenic import InputMessageContent, ReplyMarkup


class InlineQueryResultCachedVideo(InlineQueryResult):
    """
    Represents a link to a video file stored on the TeleGenic servers. By default, this video file
    will be sent by the user with an optional caption. Alternatively, you can use
    :attr:`input_message_content` to send a message with the specified content instead
    of the video.

    Args:
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        video_file_id (:obj:`str`): A valid file identifier for the video file.
        title (:obj:`str`): Title for the result.
        description (:obj:`str`, optional): Short description of the result.
        caption (:obj:`str`, optional): Caption of the video to be sent, 0-1024 characters after
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
            message to be sent instead of the video.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        type (:obj:`str`): 'video'.
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        video_file_id (:obj:`str`): A valid file identifier for the video file.
        title (:obj:`str`): Title for the result.
        description (:obj:`str`): Optional. Short description of the result.
        caption (:obj:`str`): Optional. Caption of the video to be sent, 0-1024 characters after
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
            message to be sent instead of the video.

    """

    __slots__ = (
        'reply_markup',
        'caption_entities',
        'caption',
        'title',
        'description',
        'parse_mode',
        'input_message_content',
        'video_file_id',
    )

    def __init__(
        self,
        id: str,  # pylint: disable=W0622
        video_file_id: str,
        title: str,
        description: str = None,
        caption: str = None,
        reply_markup: 'ReplyMarkup' = None,
        input_message_content: 'InputMessageContent' = None,
        parse_mode: ODVInput[str] = DEFAULT_NONE,
        caption_entities: Union[Tuple[MessageEntity, ...], List[MessageEntity]] = None,
        **_kwargs: Any,
    ):
        # Required
        super().__init__('video', id)
        self.video_file_id = video_file_id
        self.title = title

        # Optionals
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
