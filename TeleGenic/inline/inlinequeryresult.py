"""This module contains the classes that represent TeleGenic InlineQueryResult."""

from typing import Any

from TeleGenic import TeleGenicObject
from TeleGenic.utils.types import JSONDict


class InlineQueryResult(TeleGenicObject):
    """Baseclass for the InlineQueryResult* classes.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`id` is equal.

    Note:
        All URLs passed in inline query results will be available to end users and therefore must
        be assumed to be *public*.

    Args:
        type (:obj:`str`): Type of the result.
        id (:obj:`str`): Unique identifier for this result, 1-64 Bytes.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        type (:obj:`str`): Type of the result.
        id (:obj:`str`): Unique identifier for this result, 1-64 Bytes.

    """

    __slots__ = ('type', 'id', '_id_attrs')

    def __init__(self, type: str, id: str, **_kwargs: Any):
        # Required
        self.type = str(type)
        self.id = str(id)  # pylint: disable=C0103

        self._id_attrs = (self.id,)

    def to_dict(self) -> JSONDict:
        """See :meth:`TeleGenic.TeleGenicObject.to_dict`."""
        data = super().to_dict()

        # pylint: disable=E1101
        if (
            hasattr(self, 'caption_entities')
            and self.caption_entities  # type: ignore[attr-defined]
        ):
            data['caption_entities'] = [
                ce.to_dict() for ce in self.caption_entities  # type: ignore[attr-defined]
            ]

        return data
