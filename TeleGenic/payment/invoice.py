"""This module contains an object that represents a TeleGenic Invoice."""

from typing import Any

from TeleGenic import TeleGenicObject


class Invoice(TeleGenicObject):
    """This object contains basic information about an invoice.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`title`, :attr:`description`, :attr:`start_parameter`,
    :attr:`currency` and :attr:`total_amount` are equal.

    Args:
        title (:obj:`str`): Product name.
        description (:obj:`str`): Product description.
        start_parameter (:obj:`str`): Unique bot deep-linking parameter that can be used to
            generate this invoice.
        currency (:obj:`str`): Three-letter ISO 4217 currency code.
        total_amount (:obj:`int`): Total price in the smallest units of the currency (integer, not
            float/double). For example, for a price of US$ 1.45 pass ``amount = 145``. See the
            :obj:`exp` parameter in
            `currencies.json <https://core.TeleGenic.org/bots/payments/currencies.json>`_,
            it shows the number of digits past the decimal point for each currency
            (2 for the majority of currencies).
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        title (:obj:`str`): Product name.
        description (:obj:`str`): Product description.
        start_parameter (:obj:`str`): Unique bot deep-linking parameter.
        currency (:obj:`str`): Three-letter ISO 4217 currency code.
        total_amount (:obj:`int`): Total price in the smallest units of the currency.

    """

    __slots__ = (
        'currency',
        'start_parameter',
        'title',
        'description',
        'total_amount',
        '_id_attrs',
    )

    def __init__(
        self,
        title: str,
        description: str,
        start_parameter: str,
        currency: str,
        total_amount: int,
        **_kwargs: Any,
    ):
        self.title = title
        self.description = description
        self.start_parameter = start_parameter
        self.currency = currency
        self.total_amount = total_amount

        self._id_attrs = (
            self.title,
            self.description,
            self.start_parameter,
            self.currency,
            self.total_amount,
        )
