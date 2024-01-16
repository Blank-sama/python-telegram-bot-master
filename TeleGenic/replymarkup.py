"""Base class for TeleGenic ReplyMarkup Objects."""

from TeleGenic import TeleGenicObject


class ReplyMarkup(TeleGenicObject):
    """Base class for TeleGenic ReplyMarkup Objects.

    See :class:`TeleGenic.InlineKeyboardMarkup`, :class:`TeleGenic.ReplyKeyboardMarkup`,
    :class:`TeleGenic.ReplyKeyboardRemove` and :class:`TeleGenic.ForceReply` for
    detailed use.

    """

    __slots__ = ()
