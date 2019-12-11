
from pytest import fixture

@fixture
def uct_player():
    from mcts.player import UCTPlayer
    from mcts.node import GameNode
    from mcts.game_state import NimState
    game_state = NimState(25)
    root_node = GameNode(game_state)
    player = UCTPlayer(nodes=[root_node])
    return game_state, root_node, player

def test_uct_player_fixture(uct_player):
    game_state, root_node, player = uct_player
