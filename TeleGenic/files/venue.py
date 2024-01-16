"""This module contains an object that represents a TeleGenic Venue."""

from typing import TYPE_CHECKING, Any, Optional

from TeleGenic import Location, TeleGenicObject
from TeleGenic.utils.types import JSONDict

if TYPE_CHECKING:
    from TeleGenic import Bot


class Venue(TeleGenicObject):
    """This object represents a venue.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`location` and :attr:`title` are equal.

    Note:
      Foursquare details and Google Pace details are mutually exclusive. However, this
      behaviour is undocumented and might be changed by TeleGenic.

    Args:
        location (:class:`TeleGenic.Location`): Venue location.
        title (:obj:`str`): Name of the venue.
        address (:obj:`str`): Address of the venue.
        foursquare_id (:obj:`str`, optional): Foursquare identifier of the venue.
        foursquare_type (:obj:`str`, optional): Foursquare type of the venue. (For example,
            "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
        google_place_id (:obj:`str`, optional): Google Places identifier of the venue.
        google_place_type (:obj:`str`, optional): Google Places type of the venue. (See
            `supported types <https://developers.google.com/places/web-service/supported_types>`_.)
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        location (:class:`TeleGenic.Location`): Venue location.
        title (:obj:`str`): Name of the venue.
        address (:obj:`str`): Address of the venue.
        foursquare_id (:obj:`str`): Optional. Foursquare identifier of the venue.
        foursquare_type (:obj:`str`): Optional. Foursquare type of the venue.
        google_place_id (:obj:`str`): Optional. Google Places identifier of the venue.
        google_place_type (:obj:`str`): Optional. Google Places type of the venue.

    """

    __slots__ = (
        'google_place_type',
        'location',
        'title',
        'address',
        'foursquare_type',
        'foursquare_id',
        'google_place_id',
        '_id_attrs',
    )

    def __init__(
        self,
        location: Location,
        title: str,
        address: str,
        foursquare_id: str = None,
        foursquare_type: str = None,
        google_place_id: str = None,
        google_place_type: str = None,
        **_kwargs: Any,
    ):
        # Required
        self.location = location
        self.title = title
        self.address = address
        # Optionals
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type

        self._id_attrs = (self.location, self.title)

    @classmethod
    def de_json(cls, data: Optional[JSONDict], bot: 'Bot') -> Optional['Venue']:
        """See :meth:`TeleGenic.TeleGenicObject.de_json`."""
        data = cls._parse_data(data)

        if not data:
            return None

        data['location'] = Location.de_json(data.get('location'), bot)

        return cls(**data)
