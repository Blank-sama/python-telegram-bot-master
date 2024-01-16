import pytest

from telegram import LoginUrl


@pytest.fixture(scope='class')
def login_url():
    return LoginUrl(
        url=TestLoginUrl.url,
        forward_text=TestLoginUrl.forward_text,
        bot_username=TestLoginUrl.bot_username,
        request_write_access=TestLoginUrl.request_write_access,
    )


class TestLoginUrl:
    url = "http://www.google.com"
    forward_text = "Send me forward!"
    bot_username = "botname"
    request_write_access = True

    def test_slot_behaviour(self, login_url, recwarn, mro_slots):
        for attr in login_url.__slots__:
            assert getattr(login_url, attr, 'err') != 'err', f"got extra slot '{attr}'"
        assert not login_url.__dict__, f"got missing slot(s): {login_url.__dict__}"
        assert len(mro_slots(login_url)) == len(set(mro_slots(login_url))), "duplicate slot"
        login_url.custom, login_url.url = 'should give warning', self.url
        assert len(recwarn) == 1 and 'custom' in str(recwarn[0].message), recwarn.list

    def test_to_dict(self, login_url):
        login_url_dict = login_url.to_dict()

        assert isinstance(login_url_dict, dict)
        assert login_url_dict['url'] == self.url
        assert login_url_dict['forward_text'] == self.forward_text
        assert login_url_dict['bot_username'] == self.bot_username
        assert login_url_dict['request_write_access'] == self.request_write_access

    def test_equality(self):
        a = LoginUrl(self.url, self.forward_text, self.bot_username, self.request_write_access)
        b = LoginUrl(self.url, self.forward_text, self.bot_username, self.request_write_access)
        c = LoginUrl(self.url)
        d = LoginUrl("text.com", self.forward_text, self.bot_username, self.request_write_access)

        assert a == b
        assert hash(a) == hash(b)
        assert a is not b

        assert a == c
        assert hash(a) == hash(c)

        assert a != d
        assert hash(a) != hash(d)
