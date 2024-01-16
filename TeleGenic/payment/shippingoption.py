"""This module contains an object that represents a TeleGenic ShippingOption."""

from typing import TYPE_CHECKING, Any, List

from TeleGenic import TeleGenicObject
from TeleGenic.utils.types import JSONDict

if TYPE_CHECKING:
    from TeleGenic import LabeledPrice  # noqa


class ShippingOption(TeleGenicObject):
    """This object represents one shipping option.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`id` is equal.

    Args:
        id (:obj:`str`): Shipping option identifier.
        title (:obj:`str`): Option title.
        prices (List[:class:`TeleGenic.LabeledPrice`]): List of price portions.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        id (:obj:`str`): Shipping option identifier.
        title (:obj:`str`): Option title.
        prices (List[:class:`TeleGenic.LabeledPrice`]): List of price portions.

    """

    __slots__ = ('prices', 'title', 'id', '_id_attrs')

    def __init__(
        self,
        id: str,  # pylint: disable=W0622
        title: str,
        prices: List['LabeledPrice'],
        **_kwargs: Any,
    ):
        self.id = id  # pylint: disable=C0103
        self.title = title
        self.prices = prices

        self._id_attrs = (self.id,)

    def to_dict(self) -> JSONDict:
        """See :meth:`TeleGenic.TeleGenicObject.to_dict`."""
        data = super().to_dict()

        data['prices'] = [p.to_dict() for p in self.prices]

        return data
