import pytest

from TeleGenic import GameHighScore, User


@pytest.fixture(scope='class')
def game_highscore():
    return GameHighScore(
        TestGameHighScore.position, TestGameHighScore.user, TestGameHighScore.score
    )


class TestGameHighScore:
    position = 12
    user = User(2, 'test user', False)
    score = 42

    def test_slot_behaviour(self, game_highscore, recwarn, mro_slots):
        for attr in game_highscore.__slots__:
            assert getattr(game_highscore, attr, 'err') != 'err', f"got extra slot '{attr}'"
        assert not game_highscore.__dict__, f"got missing slot(s): {game_highscore.__dict__}"
        assert len(mro_slots(game_highscore)) == len(set(mro_slots(game_highscore))), "same slot"
        game_highscore.custom, game_highscore.position = 'should give warning', self.position
        assert len(recwarn) == 1 and 'custom' in str(recwarn[0].message), recwarn.list

    def test_de_json(self, bot):
        json_dict = {'position': self.position, 'user': self.user.to_dict(), 'score': self.score}
        highscore = GameHighScore.de_json(json_dict, bot)

        assert highscore.position == self.position
        assert highscore.user == self.user
        assert highscore.score == self.score

    def test_to_dict(self, game_highscore):
        game_highscore_dict = game_highscore.to_dict()

        assert isinstance(game_highscore_dict, dict)
        assert game_highscore_dict['position'] == game_highscore.position
        assert game_highscore_dict['user'] == game_highscore.user.to_dict()
        assert game_highscore_dict['score'] == game_highscore.score

    def test_equality(self):
        a = GameHighScore(1, User(2, 'test user', False), 42)
        b = GameHighScore(1, User(2, 'test user', False), 42)
        c = GameHighScore(2, User(2, 'test user', False), 42)
        d = GameHighScore(1, User(3, 'test user', False), 42)
        e = User(3, 'test user', False)

        assert a == b
        assert hash(a) == hash(b)

        assert a != c
        assert hash(a) != hash(c)

        assert a != d
        assert hash(a) != hash(d)

        assert a != e
        assert hash(a) != hash(e)
