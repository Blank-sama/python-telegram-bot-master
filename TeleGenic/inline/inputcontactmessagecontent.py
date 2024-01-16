"""This module contains the classes that represent TeleGenic InputContactMessageContent."""

from typing import Any

from TeleGenic import InputMessageContent


class InputContactMessageContent(InputMessageContent):
    """Represents the content of a contact message to be sent as the result of an inline query.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`phone_number` is equal.

    Args:
        phone_number (:obj:`str`): Contact's phone number.
        first_name (:obj:`str`): Contact's first name.
        last_name (:obj:`str`, optional): Contact's last name.
        vcard (:obj:`str`, optional): Additional data about the contact in the form of a vCard,
            0-2048 bytes.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        phone_number (:obj:`str`): Contact's phone number.
        first_name (:obj:`str`): Contact's first name.
        last_name (:obj:`str`): Optional. Contact's last name.
        vcard (:obj:`str`): Optional. Additional data about the contact in the form of a vCard,
            0-2048 bytes.

    """

    __slots__ = ('vcard', 'first_name', 'last_name', 'phone_number', '_id_attrs')

    def __init__(
        self,
        phone_number: str,
        first_name: str,
        last_name: str = None,
        vcard: str = None,
        **_kwargs: Any,
    ):
        # Required
        self.phone_number = phone_number
        self.first_name = first_name
        # Optionals
        self.last_name = last_name
        self.vcard = vcard

        self._id_attrs = (self.phone_number,)
