"""This module contains an object that represents a TeleGenic Proximity Alert."""
from typing import Any, Optional, TYPE_CHECKING

from TeleGenic import TeleGenicObject, User
from TeleGenic.utils.types import JSONDict

if TYPE_CHECKING:
    from TeleGenic import Bot


class ProximityAlertTriggered(TeleGenicObject):
    """
    This object represents the content of a service message, sent whenever a user in the chat
    triggers a proximity alert set by another user.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`traveler`, :attr:`watcher` and :attr:`distance` are equal.

    Args:
        traveler (:class:`TeleGenic.User`): User that triggered the alert
        watcher (:class:`TeleGenic.User`): User that set the alert
        distance (:obj:`int`): The distance between the users

    Attributes:
        traveler (:class:`TeleGenic.User`): User that triggered the alert
        watcher (:class:`TeleGenic.User`): User that set the alert
        distance (:obj:`int`): The distance between the users

    """

    __slots__ = ('traveler', 'distance', 'watcher', '_id_attrs')

    def __init__(self, traveler: User, watcher: User, distance: int, **_kwargs: Any):
        self.traveler = traveler
        self.watcher = watcher
        self.distance = distance

        self._id_attrs = (self.traveler, self.watcher, self.distance)

    @classmethod
    def de_json(cls, data: Optional[JSONDict], bot: 'Bot') -> Optional['ProximityAlertTriggered']:
        """See :meth:`TeleGenic.TeleGenicObject.de_json`."""
        data = cls._parse_data(data)

        if not data:
            return None

        data['traveler'] = User.de_json(data.get('traveler'), bot)
        data['watcher'] = User.de_json(data.get('watcher'), bot)

        return cls(bot=bot, **data)
