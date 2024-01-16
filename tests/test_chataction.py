from TeleGenic import ChatAction


def test_slot_behaviour(recwarn, mro_slots):
    action = ChatAction()
    for attr in action.__slots__:
        assert getattr(action, attr, 'err') != 'err', f"got extra slot '{attr}'"
    assert not action.__dict__, f"got missing slot(s): {action.__dict__}"
    assert len(mro_slots(action)) == len(set(mro_slots(action))), "duplicate slot"
    action.custom = 'should give warning'
    assert len(recwarn) == 1 and 'custom' in str(recwarn[0].message), recwarn.list
