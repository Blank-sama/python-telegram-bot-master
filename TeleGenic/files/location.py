"""This module contains an object that represents a TeleGenic Location."""

from typing import Any

from TeleGenic import TeleGenicObject


class Location(TeleGenicObject):
    """This object represents a point on the map.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`longitute` and :attr:`latitude` are equal.

    Args:
        longitude (:obj:`float`): Longitude as defined by sender.
        latitude (:obj:`float`): Latitude as defined by sender.
        horizontal_accuracy (:obj:`float`, optional): The radius of uncertainty for the location,
            measured in meters; 0-1500.
        live_period (:obj:`int`, optional): Time relative to the message sending date, during which
            the location can be updated, in seconds. For active live locations only.
        heading (:obj:`int`, optional): The direction in which user is moving, in degrees; 1-360.
            For active live locations only.
        proximity_alert_radius (:obj:`int`, optional): Maximum distance for proximity alerts about
            approaching another chat member, in meters. For sent live locations only.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        longitude (:obj:`float`): Longitude as defined by sender.
        latitude (:obj:`float`): Latitude as defined by sender.
        horizontal_accuracy (:obj:`float`): Optional. The radius of uncertainty for the location,
            measured in meters.
        live_period (:obj:`int`): Optional. Time relative to the message sending date, during which
            the location can be updated, in seconds. For active live locations only.
        heading (:obj:`int`): Optional. The direction in which user is moving, in degrees.
            For active live locations only.
        proximity_alert_radius (:obj:`int`): Optional. Maximum distance for proximity alerts about
            approaching another chat member, in meters. For sent live locations only.

    """

    __slots__ = (
        'longitude',
        'horizontal_accuracy',
        'proximity_alert_radius',
        'live_period',
        'latitude',
        'heading',
        '_id_attrs',
    )

    def __init__(
        self,
        longitude: float,
        latitude: float,
        horizontal_accuracy: float = None,
        live_period: int = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        **_kwargs: Any,
    ):
        # Required
        self.longitude = float(longitude)
        self.latitude = float(latitude)

        # Optionals
        self.horizontal_accuracy = float(horizontal_accuracy) if horizontal_accuracy else None
        self.live_period = int(live_period) if live_period else None
        self.heading = int(heading) if heading else None
        self.proximity_alert_radius = (
            int(proximity_alert_radius) if proximity_alert_radius else None
        )

        self._id_attrs = (self.longitude, self.latitude)
