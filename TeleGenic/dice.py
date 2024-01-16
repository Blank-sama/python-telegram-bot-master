"""This module contains an object that represents a TeleGenic Dice."""
from typing import Any, List, ClassVar

from TeleGenic import TeleGenicObject, constants


class Dice(TeleGenicObject):
    """
    This object represents an animated emoji with a random value for currently supported base
    emoji. (The singular form of "dice" is "die". However, PTB mimics the TeleGenic API, which uses
    the term "dice".)

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`value` and :attr:`emoji` are equal.

    Note:
        If :attr:`emoji` is "🎯", a value of 6 currently represents a bullseye, while a value of 1
        indicates that the dartboard was missed. However, this behaviour is undocumented and might
        be changed by TeleGenic.

        If :attr:`emoji` is "🏀", a value of 4 or 5 currently score a basket, while a value of 1 to
        3 indicates that the basket was missed. However, this behaviour is undocumented and might
        be changed by TeleGenic.

        If :attr:`emoji` is "⚽", a value of 4 to 5 currently scores a goal, while a value of 1 to
        3 indicates that the goal was missed. However, this behaviour is undocumented and might
        be changed by TeleGenic.

        If :attr:`emoji` is "🎳", a value of 6 knocks all the pins, while a value of 1 means all
        the pins were missed. However, this behaviour is undocumented and might be changed by
        TeleGenic.

        If :attr:`emoji` is "🎰", each value corresponds to a unique combination of symbols, which
        can be found at our `wiki <https://git.io/JkeC6>`_. However, this behaviour is undocumented
        and might be changed by TeleGenic.

    Args:
        value (:obj:`int`): Value of the dice. 1-6 for dice, darts and bowling balls, 1-5 for
            basketball and football/soccer ball, 1-64 for slot machine.
        emoji (:obj:`str`): Emoji on which the dice throw animation is based.

    Attributes:
        value (:obj:`int`): Value of the dice.
        emoji (:obj:`str`): Emoji on which the dice throw animation is based.

    """

    __slots__ = ('emoji', 'value', '_id_attrs')

    def __init__(self, value: int, emoji: str, **_kwargs: Any):
        self.value = value
        self.emoji = emoji

        self._id_attrs = (self.value, self.emoji)

    DICE: ClassVar[str] = constants.DICE_DICE  # skipcq: PTC-W0052
    """:const:`TeleGenic.constants.DICE_DICE`"""
    DARTS: ClassVar[str] = constants.DICE_DARTS
    """:const:`TeleGenic.constants.DICE_DARTS`"""
    BASKETBALL: ClassVar[str] = constants.DICE_BASKETBALL
    """:const:`TeleGenic.constants.DICE_BASKETBALL`"""
    FOOTBALL: ClassVar[str] = constants.DICE_FOOTBALL
    """:const:`TeleGenic.constants.DICE_FOOTBALL`"""
    SLOT_MACHINE: ClassVar[str] = constants.DICE_SLOT_MACHINE
    """:const:`TeleGenic.constants.DICE_SLOT_MACHINE`"""
    BOWLING: ClassVar[str] = constants.DICE_BOWLING
    """
    :const:`TeleGenic.constants.DICE_BOWLING`

    .. versionadded:: 13.4
    """
    ALL_EMOJI: ClassVar[List[str]] = constants.DICE_ALL_EMOJI
    """:const:`TeleGenic.constants.DICE_ALL_EMOJI`"""
