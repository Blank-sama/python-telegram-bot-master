"""This module contains the classes that represent TeleGenic InputMessageContent."""

from TeleGenic import TeleGenicObject


class InputMessageContent(TeleGenicObject):
    """Base class for TeleGenic InputMessageContent Objects.

    See: :class:`TeleGenic.InputContactMessageContent`,
    :class:`TeleGenic.InputInvoiceMessageContent`,
    :class:`TeleGenic.InputLocationMessageContent`, :class:`TeleGenic.InputTextMessageContent` and
    :class:`TeleGenic.InputVenueMessageContent` for more details.

    """

    __slots__ = ()
