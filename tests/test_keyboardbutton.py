import pytest

from telegram import KeyboardButton, InlineKeyboardButton
from telegram.keyboardbuttonpolltype import KeyboardButtonPollType


@pytest.fixture(scope='class')
def keyboard_button():
    return KeyboardButton(
        TestKeyboardButton.text,
        request_location=TestKeyboardButton.request_location,
        request_contact=TestKeyboardButton.request_contact,
        request_poll=TestKeyboardButton.request_poll,
    )


class TestKeyboardButton:
    text = 'text'
    request_location = True
    request_contact = True
    request_poll = KeyboardButtonPollType("quiz")

    def test_slot_behaviour(self, keyboard_button, recwarn, mro_slots):
        inst = keyboard_button
        for attr in inst.__slots__:
            assert getattr(inst, attr, 'err') != 'err', f"got extra slot '{attr}'"
        assert not inst.__dict__, f"got missing slot(s): {inst.__dict__}"
        assert len(mro_slots(inst)) == len(set(mro_slots(inst))), "duplicate slot"
        inst.custom, inst.text = 'should give warning', self.text
        assert len(recwarn) == 1 and 'custom' in str(recwarn[0].message), recwarn.list

    def test_expected_values(self, keyboard_button):
        assert keyboard_button.text == self.text
        assert keyboard_button.request_location == self.request_location
        assert keyboard_button.request_contact == self.request_contact
        assert keyboard_button.request_poll == self.request_poll

    def test_to_dict(self, keyboard_button):
        keyboard_button_dict = keyboard_button.to_dict()

        assert isinstance(keyboard_button_dict, dict)
        assert keyboard_button_dict['text'] == keyboard_button.text
        assert keyboard_button_dict['request_location'] == keyboard_button.request_location
        assert keyboard_button_dict['request_contact'] == keyboard_button.request_contact
        assert keyboard_button_dict['request_poll'] == keyboard_button.request_poll.to_dict()

    def test_equality(self):
        a = KeyboardButton('test', request_contact=True)
        b = KeyboardButton('test', request_contact=True)
        c = KeyboardButton('Test', request_location=True)
        d = InlineKeyboardButton('test', callback_data='test')

        assert a == b
        assert hash(a) == hash(b)

        assert a != c
        assert hash(a) != hash(c)

        assert a != d
        assert hash(a) != hash(d)
