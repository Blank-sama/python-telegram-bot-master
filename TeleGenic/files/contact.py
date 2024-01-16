"""This module contains an object that represents a TeleGenic Contact."""

from typing import Any

from TeleGenic import TeleGenicObject


class Contact(TeleGenicObject):
    """This object represents a phone contact.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`phone_number` is equal.

    Args:
        phone_number (:obj:`str`): Contact's phone number.
        first_name (:obj:`str`): Contact's first name.
        last_name (:obj:`str`, optional): Contact's last name.
        user_id (:obj:`int`, optional): Contact's user identifier in TeleGenic.
        vcard (:obj:`str`, optional): Additional data about the contact in the form of a vCard.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        phone_number (:obj:`str`): Contact's phone number.
        first_name (:obj:`str`): Contact's first name.
        last_name (:obj:`str`): Optional. Contact's last name.
        user_id (:obj:`int`): Optional. Contact's user identifier in TeleGenic.
        vcard (:obj:`str`): Optional. Additional data about the contact in the form of a vCard.

    """

    __slots__ = ('vcard', 'user_id', 'first_name', 'last_name', 'phone_number', '_id_attrs')

    def __init__(
        self,
        phone_number: str,
        first_name: str,
        last_name: str = None,
        user_id: int = None,
        vcard: str = None,
        **_kwargs: Any,
    ):
        # Required
        self.phone_number = str(phone_number)
        self.first_name = first_name
        # Optionals
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard

        self._id_attrs = (self.phone_number,)
