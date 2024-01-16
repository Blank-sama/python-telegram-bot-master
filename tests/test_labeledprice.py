import pytest

from telegram import LabeledPrice, Location


@pytest.fixture(scope='class')
def labeled_price():
    return LabeledPrice(TestLabeledPrice.label, TestLabeledPrice.amount)


class TestLabeledPrice:
    label = 'label'
    amount = 100

    def test_slot_behaviour(self, labeled_price, recwarn, mro_slots):
        inst = labeled_price
        for attr in inst.__slots__:
            assert getattr(inst, attr, 'err') != 'err', f"got extra slot '{attr}'"
        assert not inst.__dict__, f"got missing slot(s): {inst.__dict__}"
        assert len(mro_slots(inst)) == len(set(mro_slots(inst))), "duplicate slot"
        inst.custom, inst.label = 'should give warning', self.label
        assert len(recwarn) == 1 and 'custom' in str(recwarn[0].message), recwarn.list

    def test_expected_values(self, labeled_price):
        assert labeled_price.label == self.label
        assert labeled_price.amount == self.amount

    def test_to_dict(self, labeled_price):
        labeled_price_dict = labeled_price.to_dict()

        assert isinstance(labeled_price_dict, dict)
        assert labeled_price_dict['label'] == labeled_price.label
        assert labeled_price_dict['amount'] == labeled_price.amount

    def test_equality(self):
        a = LabeledPrice('label', 100)
        b = LabeledPrice('label', 100)
        c = LabeledPrice('Label', 101)
        d = Location(123, 456)

        assert a == b
        assert hash(a) == hash(b)

        assert a != c
        assert hash(a) != hash(c)

        assert a != d
        assert hash(a) != hash(d)
