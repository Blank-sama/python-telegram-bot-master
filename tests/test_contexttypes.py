import pytest

from TeleGenic.ext import ContextTypes, CallbackContext


class SubClass(CallbackContext):
    pass


class TestContextTypes:
    def test_slot_behaviour(self, mro_slots):
        instance = ContextTypes()
        for attr in instance.__slots__:
            assert getattr(instance, attr, 'err') != 'err', f"got extra slot '{attr}'"
        assert len(mro_slots(instance)) == len(set(mro_slots(instance))), "duplicate slot"
        with pytest.raises(AttributeError):
            instance.custom

    def test_data_init(self):
        ct = ContextTypes(SubClass, int, float, bool)
        assert ct.context is SubClass
        assert ct.bot_data is int
        assert ct.chat_data is float
        assert ct.user_data is bool

        with pytest.raises(ValueError, match='subclass of CallbackContext'):
            ContextTypes(context=bool)

    def test_data_assignment(self):
        ct = ContextTypes()

        with pytest.raises(AttributeError):
            ct.bot_data = bool
        with pytest.raises(AttributeError):
            ct.user_data = bool
        with pytest.raises(AttributeError):
            ct.chat_data = bool
