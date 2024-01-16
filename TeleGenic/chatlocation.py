"""This module contains an object that represents a location to which a chat is connected."""

from typing import TYPE_CHECKING, Any, Optional

from TeleGenic import TeleGenicObject
from TeleGenic.utils.types import JSONDict

from .files.location import Location

if TYPE_CHECKING:
    from TeleGenic import Bot


class ChatLocation(TeleGenicObject):
    """This object represents a location to which a chat is connected.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`location` is equal.

    Args:
        location (:class:`TeleGenic.Location`): The location to which the supergroup is connected.
            Can't be a live location.
        address (:obj:`str`): Location address; 1-64 characters, as defined by the chat owner
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        location (:class:`TeleGenic.Location`): The location to which the supergroup is connected.
        address (:obj:`str`): Location address, as defined by the chat owner

    """

    __slots__ = ('location', '_id_attrs', 'address')

    def __init__(
        self,
        location: Location,
        address: str,
        **_kwargs: Any,
    ):
        self.location = location
        self.address = address

        self._id_attrs = (self.location,)

    @classmethod
    def de_json(cls, data: Optional[JSONDict], bot: 'Bot') -> Optional['ChatLocation']:
        """See :meth:`TeleGenic.TeleGenicObject.de_json`."""
        data = cls._parse_data(data)

        if not data:
            return None

        data['location'] = Location.de_json(data.get('location'), bot)

        return cls(bot=bot, **data)
