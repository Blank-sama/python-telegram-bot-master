"""This module contains an object that represents a TeleGenic OrderInfo."""

from typing import TYPE_CHECKING, Any, Optional

from TeleGenic import ShippingAddress, TeleGenicObject
from TeleGenic.utils.types import JSONDict

if TYPE_CHECKING:
    from TeleGenic import Bot


class OrderInfo(TeleGenicObject):
    """This object represents information about an order.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`name`, :attr:`phone_number`, :attr:`email` and
    :attr:`shipping_address` are equal.

    Args:
        name (:obj:`str`, optional): User name.
        phone_number (:obj:`str`, optional): User's phone number.
        email (:obj:`str`, optional): User email.
        shipping_address (:class:`TeleGenic.ShippingAddress`, optional): User shipping address.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        name (:obj:`str`): Optional. User name.
        phone_number (:obj:`str`): Optional. User's phone number.
        email (:obj:`str`): Optional. User email.
        shipping_address (:class:`TeleGenic.ShippingAddress`): Optional. User shipping address.

    """

    __slots__ = ('email', 'shipping_address', 'phone_number', 'name', '_id_attrs')

    def __init__(
        self,
        name: str = None,
        phone_number: str = None,
        email: str = None,
        shipping_address: str = None,
        **_kwargs: Any,
    ):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = shipping_address

        self._id_attrs = (self.name, self.phone_number, self.email, self.shipping_address)

    @classmethod
    def de_json(cls, data: Optional[JSONDict], bot: 'Bot') -> Optional['OrderInfo']:
        """See :meth:`TeleGenic.TeleGenicObject.de_json`."""
        data = cls._parse_data(data)

        if not data:
            return cls()

        data['shipping_address'] = ShippingAddress.de_json(data.get('shipping_address'), bot)

        return cls(**data)
