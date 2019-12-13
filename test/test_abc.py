
import pytest
from games.abc import UUIDPlayer, UUIDHash, AlternatingTwoPlayerGame, GameState, GameMove
from games.exceptions import WrongPlayer

class TrivialUUIDPlayer(UUIDPlayer):
    def play(self, game):
        pass

class TrivialMove(GameMove):
    pass

class TrivialGameState(GameState):
    pass

class TrivialAlternatingTwoPlayerGame(AlternatingTwoPlayerGame):

    def _make_move(self, player, move):
        pass

    @property
    def current_state(self):
        return TrivialGameState()

def test_UUIDPlayer_equality():
    p = TrivialUUIDPlayer()
    assert p == p

def test_UUIDPlayer_inequality():
    p1 = TrivialUUIDPlayer()
    p2 = TrivialUUIDPlayer()
    assert p1 != p2

def test_UUIDPlayer_hash_equality():
    p = TrivialUUIDPlayer()
    assert hash(p) == hash(p)

def test_UUIDPlayer_hash_inequality():
    p1 = TrivialUUIDPlayer()
    p2 = TrivialUUIDPlayer()
    assert hash(p1) != hash(p2)

@pytest.fixture
def trivial_alternating_game():
    p1 = TrivialUUIDPlayer()
    p2 = TrivialUUIDPlayer()
    g = TrivialAlternatingTwoPlayerGame(p1, p2)
    return p1, p2, g

def test_AlternatingTwoPlayerGame_starting_player(trivial_alternating_game):
    p1, p2, g = trivial_alternating_game
    assert g.current_player == p1

def test_AlternatingTwoPlayerGame_switch_players(trivial_alternating_game):
    p1, p2, g = trivial_alternating_game
    g.make_move(p1, TrivialMove())
    assert g.current_player == p2

def test_AlternatingTwoPlayerGame_wrong_player1(trivial_alternating_game):
    p1, p2, g = trivial_alternating_game
    with pytest.raises(WrongPlayer):
        g.make_move(p2, TrivialMove())

def test_AlternatingTwoPlayerGame_wrong_player2(trivial_alternating_game):
    p1, p2, g = trivial_alternating_game
    g.make_move(p1, TrivialMove())
    with pytest.raises(WrongPlayer):
        g.make_move(p1, TrivialMove())
