"""This module contains the classes that represent TeleGenic InputTextMessageContent."""

from typing import Any, Union, Tuple, List

from TeleGenic import InputMessageContent, MessageEntity
from TeleGenic.utils.helpers import DEFAULT_NONE
from TeleGenic.utils.types import JSONDict, ODVInput


class InputTextMessageContent(InputMessageContent):
    """
    Represents the content of a text message to be sent as the result of an inline query.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`message_text` is equal.

    Args:
        message_text (:obj:`str`): Text of the message to be sent, 1-4096 characters after entities
            parsing. Also found as :attr:`TeleGenic.constants.MAX_MESSAGE_LENGTH`.
        parse_mode (:obj:`str`, optional): Send Markdown or HTML, if you want TeleGenic apps to show
            bold, italic, fixed-width text or inline URLs in your bot's message. See the constants
            in :class:`TeleGenic.ParseMode` for the available modes.
        entities (List[:class:`TeleGenic.MessageEntity`], optional): List of special
            entities that appear in the caption, which can be specified instead of
            :attr:`parse_mode`.
        disable_web_page_preview (:obj:`bool`, optional): Disables link previews for links in the
            sent message.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        message_text (:obj:`str`): Text of the message to be sent, 1-4096 characters after entities
            parsing.
        parse_mode (:obj:`str`): Optional. Send Markdown or HTML, if you want TeleGenic apps to show
            bold, italic, fixed-width text or inline URLs in your bot's message. See the constants
            in :class:`TeleGenic.ParseMode` for the available modes.
        entities (List[:class:`TeleGenic.MessageEntity`]): Optional. List of special
            entities that appear in the caption, which can be specified instead of
            :attr:`parse_mode`.
        disable_web_page_preview (:obj:`bool`): Optional. Disables link previews for links in the
            sent message.

    """

    __slots__ = ('disable_web_page_preview', 'parse_mode', 'entities', 'message_text', '_id_attrs')

    def __init__(
        self,
        message_text: str,
        parse_mode: ODVInput[str] = DEFAULT_NONE,
        disable_web_page_preview: ODVInput[bool] = DEFAULT_NONE,
        entities: Union[Tuple[MessageEntity, ...], List[MessageEntity]] = None,
        **_kwargs: Any,
    ):
        # Required
        self.message_text = message_text
        # Optionals
        self.parse_mode = parse_mode
        self.entities = entities
        self.disable_web_page_preview = disable_web_page_preview

        self._id_attrs = (self.message_text,)

    def to_dict(self) -> JSONDict:
        """See :meth:`TeleGenic.TeleGenicObject.to_dict`."""
        data = super().to_dict()

        if self.entities:
            data['entities'] = [ce.to_dict() for ce in self.entities]

        return data
