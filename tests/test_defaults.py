import pytest

from TeleGenic.ext import Defaults
from TeleGenic import User


class TestDefault:
    def test_slot_behaviour(self, recwarn, mro_slots):
        a = Defaults(parse_mode='HTML', quote=True)
        for attr in a.__slots__:
            assert getattr(a, attr, 'err') != 'err', f"got extra slot '{attr}'"
        assert not a.__dict__, f"got missing slot(s): {a.__dict__}"
        assert len(mro_slots(a)) == len(set(mro_slots(a))), "duplicate slot"
        a.custom, a._parse_mode = 'should give warning', a._parse_mode
        assert len(recwarn) == 1 and 'custom' in str(recwarn[0].message), recwarn.list

    def test_data_assignment(self, cdp):
        defaults = Defaults()

        with pytest.raises(AttributeError):
            defaults.parse_mode = True
        with pytest.raises(AttributeError):
            defaults.explanation_parse_mode = True
        with pytest.raises(AttributeError):
            defaults.disable_notification = True
        with pytest.raises(AttributeError):
            defaults.disable_web_page_preview = True
        with pytest.raises(AttributeError):
            defaults.allow_sending_without_reply = True
        with pytest.raises(AttributeError):
            defaults.timeout = True
        with pytest.raises(AttributeError):
            defaults.quote = True
        with pytest.raises(AttributeError):
            defaults.tzinfo = True
        with pytest.raises(AttributeError):
            defaults.block = True
        with pytest.raises(AttributeError):
            defaults.restrict_content = False
            

    def test_equality(self):
        a = Defaults(parse_mode='HTML', quote=True)
        b = Defaults(parse_mode='HTML', quote=True)
        c = Defaults(parse_mode='HTML', quote=False , restrict_content=False)
        d = Defaults(parse_mode='HTML', timeout=50, restrict_content=False)
        e = User(123, 'test_user', False)

        assert a == b
        assert hash(a) == hash(b)
        assert a is not b

        assert a != c
        assert hash(a) != hash(c)

        assert a != d
        assert hash(a) != hash(d)

        assert a != e
        assert hash(a) != hash(e)
