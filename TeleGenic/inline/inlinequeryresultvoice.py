"""This module contains the classes that represent TeleGenic InlineQueryResultVoice."""

from typing import TYPE_CHECKING, Any, Union, Tuple, List

from TeleGenic import InlineQueryResult, MessageEntity
from TeleGenic.utils.helpers import DEFAULT_NONE
from TeleGenic.utils.types import ODVInput

if TYPE_CHECKING:
    from TeleGenic import InputMessageContent, ReplyMarkup


class InlineQueryResultVoice(InlineQueryResult):
    """
    Represents a link to a voice recording in an .ogg container encoded with OPUS. By default,
    this voice recording will be sent by the user. Alternatively, you can use
    :attr:`input_message_content` to send a message with the specified content instead of the
    the voice message.

    Args:
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        voice_url (:obj:`str`): A valid URL for the voice recording.
        title (:obj:`str`): Recording title.
        caption (:obj:`str`, optional): Caption, 0-1024 characters after entities parsing.
        parse_mode (:obj:`str`, optional): Send Markdown or HTML, if you want TeleGenic apps to show
            bold, italic, fixed-width text or inline URLs in the media caption. See the constants
            in :class:`TeleGenic.ParseMode` for the available modes.
        caption_entities (List[:class:`TeleGenic.MessageEntity`], optional): List of special
            entities that appear in the caption, which can be specified instead of
            :attr:`parse_mode`.
        voice_duration (:obj:`int`, optional): Recording duration in seconds.
        reply_markup (:class:`TeleGenic.InlineKeyboardMarkup`, optional): Inline keyboard attached
            to the message.
        input_message_content (:class:`TeleGenic.InputMessageContent`, optional): Content of the
            message to be sent instead of the voice recording.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        type (:obj:`str`): 'voice'.
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        voice_url (:obj:`str`): A valid URL for the voice recording.
        title (:obj:`str`): Recording title.
        caption (:obj:`str`): Optional. Caption, 0-1024 characters after entities parsing.
        parse_mode (:obj:`str`): Optional. Send Markdown or HTML, if you want TeleGenic apps to show
            bold, italic, fixed-width text or inline URLs in the media caption. See the constants
            in :class:`TeleGenic.ParseMode` for the available modes.
        caption_entities (List[:class:`TeleGenic.MessageEntity`]): Optional. List of special
            entities that appear in the caption, which can be specified instead of
            :attr:`parse_mode`.
        voice_duration (:obj:`int`): Optional. Recording duration in seconds.
        reply_markup (:class:`TeleGenic.InlineKeyboardMarkup`): Optional. Inline keyboard attached
            to the message.
        input_message_content (:class:`TeleGenic.InputMessageContent`): Optional. Content of the
            message to be sent instead of the voice recording.

    """

    __slots__ = (
        'reply_markup',
        'caption_entities',
        'voice_duration',
        'caption',
        'title',
        'voice_url',
        'parse_mode',
        'input_message_content',
    )

    def __init__(
        self,
        id: str,  # pylint: disable=W0622
        voice_url: str,
        title: str,
        voice_duration: int = None,
        caption: str = None,
        reply_markup: 'ReplyMarkup' = None,
        input_message_content: 'InputMessageContent' = None,
        parse_mode: ODVInput[str] = DEFAULT_NONE,
        caption_entities: Union[Tuple[MessageEntity, ...], List[MessageEntity]] = None,
        **_kwargs: Any,
    ):

        # Required
        super().__init__('voice', id)
        self.voice_url = voice_url
        self.title = title

        # Optional
        self.voice_duration = voice_duration
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
