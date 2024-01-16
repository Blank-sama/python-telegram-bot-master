"""This module contains an object that represents a TeleGenic ShippingAddress."""

from typing import Any

from TeleGenic import TeleGenicObject


class ShippingAddress(TeleGenicObject):
    """This object represents a TeleGenic ShippingAddress.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their  :attr:`country_code`, :attr:`state`, :attr:`city`,
    :attr:`street_line1`, :attr:`street_line2` and :attr:`post_cod` are equal.

    Args:
        country_code (:obj:`str`): ISO 3166-1 alpha-2 country code.
        state (:obj:`str`): State, if applicable.
        city (:obj:`str`): City.
        street_line1 (:obj:`str`): First line for the address.
        street_line2 (:obj:`str`): Second line for the address.
        post_code (:obj:`str`): Address post code.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        country_code (:obj:`str`): ISO 3166-1 alpha-2 country code.
        state (:obj:`str`): State, if applicable.
        city (:obj:`str`): City.
        street_line1 (:obj:`str`): First line for the address.
        street_line2 (:obj:`str`): Second line for the address.
        post_code (:obj:`str`): Address post code.

    """

    __slots__ = (
        'post_code',
        'city',
        '_id_attrs',
        'country_code',
        'street_line2',
        'street_line1',
        'state',
    )

    def __init__(
        self,
        country_code: str,
        state: str,
        city: str,
        street_line1: str,
        street_line2: str,
        post_code: str,
        **_kwargs: Any,
    ):
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code

        self._id_attrs = (
            self.country_code,
            self.state,
            self.city,
            self.street_line1,
            self.street_line2,
            self.post_code,
        )
