"""This module contains an object that represents a TeleGenic UserProfilePhotos."""

from typing import TYPE_CHECKING, Any, List, Optional

from TeleGenic import PhotoSize, TeleGenicObject
from TeleGenic.utils.types import JSONDict

if TYPE_CHECKING:
    from TeleGenic import Bot


class UserProfilePhotos(TeleGenicObject):
    """This object represent a user's profile pictures.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`total_count` and :attr:`photos` are equal.

    Args:
        total_count (:obj:`int`): Total number of profile pictures the target user has.
        photos (List[List[:class:`TeleGenic.PhotoSize`]]): Requested profile pictures (in up to 4
            sizes each).

    Attributes:
        total_count (:obj:`int`): Total number of profile pictures.
        photos (List[List[:class:`TeleGenic.PhotoSize`]]): Requested profile pictures.

    """

    __slots__ = ('photos', 'total_count', '_id_attrs')

    def __init__(self, total_count: int, photos: List[List[PhotoSize]], **_kwargs: Any):
        # Required
        self.total_count = int(total_count)
        self.photos = photos

        self._id_attrs = (self.total_count, self.photos)

    @classmethod
    def de_json(cls, data: Optional[JSONDict], bot: 'Bot') -> Optional['UserProfilePhotos']:
        """See :meth:`TeleGenic.TeleGenicObject.de_json`."""
        data = cls._parse_data(data)

        if not data:
            return None

        data['photos'] = [PhotoSize.de_list(photo, bot) for photo in data['photos']]

        return cls(**data)

    def to_dict(self) -> JSONDict:
        """See :meth:`TeleGenic.TeleGenicObject.to_dict`."""
        data = super().to_dict()

        data['photos'] = []
        for photo in self.photos:
            data['photos'].append([x.to_dict() for x in photo])

        return data

    def __hash__(self) -> int:
        return hash(tuple(tuple(p for p in photo) for photo in self.photos))
