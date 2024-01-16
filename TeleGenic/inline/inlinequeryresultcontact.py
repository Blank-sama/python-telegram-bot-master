"""This module contains the classes that represent TeleGenic InlineQueryResultContact."""

from typing import TYPE_CHECKING, Any

from TeleGenic import InlineQueryResult

if TYPE_CHECKING:
    from TeleGenic import InputMessageContent, ReplyMarkup


class InlineQueryResultContact(InlineQueryResult):
    """
    Represents a contact with a phone number. By default, this contact will be sent by the user.
    Alternatively, you can use :attr:`input_message_content` to send a message with the specified
    content instead of the contact.

    Args:
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        phone_number (:obj:`str`): Contact's phone number.
        first_name (:obj:`str`): Contact's first name.
        last_name (:obj:`str`, optional): Contact's last name.
        vcard (:obj:`str`, optional): Additional data about the contact in the form of a vCard,
            0-2048 bytes.
        reply_markup (:class:`TeleGenic.InlineKeyboardMarkup`, optional): Inline keyboard attached
            to the message.
        input_message_content (:class:`TeleGenic.InputMessageContent`, optional): Content of the
            message to be sent instead of the contact.
        thumb_url (:obj:`str`, optional): Url of the thumbnail for the result.
        thumb_width (:obj:`int`, optional): Thumbnail width.
        thumb_height (:obj:`int`, optional): Thumbnail height.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        type (:obj:`str`): 'contact'.
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        phone_number (:obj:`str`): Contact's phone number.
        first_name (:obj:`str`): Contact's first name.
        last_name (:obj:`str`): Optional. Contact's last name.
        vcard (:obj:`str`): Optional. Additional data about the contact in the form of a vCard,
            0-2048 bytes.
        reply_markup (:class:`TeleGenic.InlineKeyboardMarkup`): Optional. Inline keyboard attached
            to the message.
        input_message_content (:class:`TeleGenic.InputMessageContent`): Optional. Content of the
            message to be sent instead of the contact.
        thumb_url (:obj:`str`): Optional. Url of the thumbnail for the result.
        thumb_width (:obj:`int`): Optional. Thumbnail width.
        thumb_height (:obj:`int`): Optional. Thumbnail height.

    """

    __slots__ = (
        'reply_markup',
        'thumb_width',
        'thumb_height',
        'vcard',
        'first_name',
        'last_name',
        'phone_number',
        'input_message_content',
        'thumb_url',
    )

    def __init__(
        self,
        id: str,  # pylint: disable=W0622
        phone_number: str,
        first_name: str,
        last_name: str = None,
        reply_markup: 'ReplyMarkup' = None,
        input_message_content: 'InputMessageContent' = None,
        thumb_url: str = None,
        thumb_width: int = None,
        thumb_height: int = None,
        vcard: str = None,
        **_kwargs: Any,
    ):
        # Required
        super().__init__('contact', id)
        self.phone_number = phone_number
        self.first_name = first_name

        # Optionals
        self.last_name = last_name
        self.vcard = vcard
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
