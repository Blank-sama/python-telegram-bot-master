from flaky import flaky

from telegram import ParseMode


class TestParseMode:
    markdown_text = '*bold* _italic_ [link](http://google.com) [name](tg://user?id=123456789).'
    html_text = (
        '<b>bold</b> <i>italic</i> <a href="http://google.com">link</a> '
        '<a href="tg://user?id=123456789">name</a>.'
    )
    formatted_text_formatted = 'bold italic link name.'

    def test_slot_behaviour(self, recwarn, mro_slots):
        inst = ParseMode()
        for attr in inst.__slots__:
            assert getattr(inst, attr, 'err') != 'err', f"got extra slot '{attr}'"
        assert not inst.__dict__, f"got missing slot(s): {inst.__dict__}"
        assert len(mro_slots(inst)) == len(set(mro_slots(inst))), "duplicate slot"
        inst.custom = 'should give warning'
        assert len(recwarn) == 1 and 'custom' in str(recwarn[0].message), recwarn.list

    @flaky(3, 1)
    def test_send_message_with_parse_mode_markdown(self, bot, chat_id):
        message = bot.send_message(
            chat_id=chat_id, text=self.markdown_text, parse_mode=ParseMode.MARKDOWN
        )

        assert message.text == self.formatted_text_formatted

    @flaky(3, 1)
    def test_send_message_with_parse_mode_html(self, bot, chat_id):
        message = bot.send_message(chat_id=chat_id, text=self.html_text, parse_mode=ParseMode.HTML)

        assert message.text == self.formatted_text_formatted
