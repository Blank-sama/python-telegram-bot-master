"""This module contains an object that represents a TeleGenic LabeledPrice."""

from typing import Any

from TeleGenic import TeleGenicObject


class LabeledPrice(TeleGenicObject):
    """This object represents a portion of the price for goods or services.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`label` and :attr:`amount` are equal.

    Args:
        label (:obj:`str`): Portion label.
        amount (:obj:`int`): Price of the product in the smallest units of the currency (integer,
            not float/double). For example, for a price of US$ 1.45 pass ``amount = 145``.
            See the :obj:`exp` parameter in
            `currencies.json <https://core.TeleGenic.org/bots/payments/currencies.json>`_,
            it shows the number of digits past the decimal point for each currency
            (2 for the majority of currencies).
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        label (:obj:`str`): Portion label.
        amount (:obj:`int`): Price of the product in the smallest units of the currency.

    """

    __slots__ = ('label', '_id_attrs', 'amount')

    def __init__(self, label: str, amount: int, **_kwargs: Any):
        self.label = label
        self.amount = amount

        self._id_attrs = (self.label, self.amount)
