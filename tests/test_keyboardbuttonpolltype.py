import pytest

from telegram import KeyboardButtonPollType, Poll


@pytest.fixture(scope='class')
def keyboard_button_poll_type():
    return KeyboardButtonPollType(TestKeyboardButtonPollType.type)


class TestKeyboardButtonPollType:
    type = Poll.QUIZ

    def test_slot_behaviour(self, keyboard_button_poll_type, recwarn, mro_slots):
        inst = keyboard_button_poll_type
        for attr in inst.__slots__:
            assert getattr(inst, attr, 'err') != 'err', f"got extra slot '{attr}'"
        assert not inst.__dict__, f"got missing slot(s): {inst.__dict__}"
        assert len(mro_slots(inst)) == len(set(mro_slots(inst))), "duplicate slot"
        inst.custom, inst.type = 'should give warning', self.type
        assert len(recwarn) == 1 and 'custom' in str(recwarn[0].message), recwarn.list

    def test_to_dict(self, keyboard_button_poll_type):
        keyboard_button_poll_type_dict = keyboard_button_poll_type.to_dict()
        assert isinstance(keyboard_button_poll_type_dict, dict)
        assert keyboard_button_poll_type_dict['type'] == self.type

    def test_equality(self):
        a = KeyboardButtonPollType(Poll.QUIZ)
        b = KeyboardButtonPollType(Poll.QUIZ)
        c = KeyboardButtonPollType(Poll.REGULAR)

        assert a == b
        assert hash(a) == hash(b)
        assert a is not b

        assert a != c
        assert hash(a) != hash(c)
