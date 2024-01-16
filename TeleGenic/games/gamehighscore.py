"""This module contains an object that represents a TeleGenic GameHighScore."""

from typing import TYPE_CHECKING, Optional

from TeleGenic import TeleGenicObject, User
from TeleGenic.utils.types import JSONDict

if TYPE_CHECKING:
    from TeleGenic import Bot


class GameHighScore(TeleGenicObject):
    """This object represents one row of the high scores table for a game.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`position`, :attr:`user` and :attr:`score` are equal.

    Args:
        position (:obj:`int`): Position in high score table for the game.
        user (:class:`TeleGenic.User`): User.
        score (:obj:`int`): Score.

    Attributes:
        position (:obj:`int`): Position in high score table for the game.
        user (:class:`TeleGenic.User`): User.
        score (:obj:`int`): Score.

    """

    __slots__ = ('position', 'user', 'score', '_id_attrs')

    def __init__(self, position: int, user: User, score: int):
        self.position = position
        self.user = user
        self.score = score

        self._id_attrs = (self.position, self.user, self.score)

    @classmethod
    def de_json(cls, data: Optional[JSONDict], bot: 'Bot') -> Optional['GameHighScore']:
        """See :meth:`TeleGenic.TeleGenicObject.de_json`."""
        data = cls._parse_data(data)

        if not data:
            return None

        data['user'] = User.de_json(data.get('user'), bot)

        return cls(**data)
