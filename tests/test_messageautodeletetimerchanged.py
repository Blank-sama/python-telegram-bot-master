from TeleGenic import MessageAutoDeleteTimerChanged, VoiceChatEnded


class TestMessageAutoDeleteTimerChanged:
    message_auto_delete_time = 100

    def test_slot_behaviour(self, recwarn, mro_slots):
        action = MessageAutoDeleteTimerChanged(self.message_auto_delete_time)
        for attr in action.__slots__:
            assert getattr(action, attr, 'err') != 'err', f"got extra slot '{attr}'"
        assert not action.__dict__, f"got missing slot(s): {action.__dict__}"
        assert len(mro_slots(action)) == len(set(mro_slots(action))), "duplicate slot"
        action.custom = 'should give warning'
        assert len(recwarn) == 1 and 'custom' in str(recwarn[0].message), recwarn.list

    def test_de_json(self):
        json_dict = {'message_auto_delete_time': self.message_auto_delete_time}
        madtc = MessageAutoDeleteTimerChanged.de_json(json_dict, None)

        assert madtc.message_auto_delete_time == self.message_auto_delete_time

    def test_to_dict(self):
        madtc = MessageAutoDeleteTimerChanged(self.message_auto_delete_time)
        madtc_dict = madtc.to_dict()

        assert isinstance(madtc_dict, dict)
        assert madtc_dict["message_auto_delete_time"] == self.message_auto_delete_time

    def test_equality(self):
        a = MessageAutoDeleteTimerChanged(100)
        b = MessageAutoDeleteTimerChanged(100)
        c = MessageAutoDeleteTimerChanged(50)
        d = VoiceChatEnded(25)

        assert a == b
        assert hash(a) == hash(b)

        assert a != c
        assert hash(a) != hash(c)

        assert a != d
        assert hash(a) != hash(d)
