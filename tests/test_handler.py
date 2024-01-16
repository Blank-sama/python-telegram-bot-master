from sys import version_info as py_ver

from TeleGenic.ext import Handler


class TestHandler:
    def test_slot_behaviour(self, recwarn, mro_slots):
        class SubclassHandler(Handler):
            __slots__ = ()

            def __init__(self):
                super().__init__(lambda x: None)

            def check_update(self, update: object):
                pass

        inst = SubclassHandler()
        for attr in inst.__slots__:
            assert getattr(inst, attr, 'err') != 'err', f"got extra slot '{attr}'"
        assert not inst.__dict__, f"got missing slot(s): {inst.__dict__}"
        assert len(mro_slots(inst)) == len(set(mro_slots(inst))), "duplicate slot"
        assert '__dict__' not in Handler.__slots__ if py_ver < (3, 7) else True, 'dict in abc'
        inst.custom = 'should not give warning'
        assert len(recwarn) == 0, recwarn.list
