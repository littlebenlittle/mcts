
from pytest import fixture

@fixture
def uct_player():
    from mcts.player import UCTPlayer
    from mcts.node import GameNode
    from mcts.game_state import NimState
    game_state = NimState(25)
    root_node = GameNode(game_state)
    player = UCTPlayer(root_node=root_node)
    return game_state, root_node, player

def test_uct_player_fixture(uct_player):
    game_state, root_node, player = uct_player

def test_player_has_root_node(uct_player):
    _, root_node, player = uct_player
    assert root_node in player.game_graph.nodes

def test_player_has_game_state(uct_player):
    game_state, _, player = uct_player
    assert game_state in player.game_states

def test_root_node_has_game_state(uct_player):
    game_state, root_node, _ = uct_player
    assert game_state == root_node.game_state

def test_game_state_next_states_in_player_game_states_after_expansion(uct_player):
    game_state, _, player = uct_player
    player.game_graph.root_node.expand()
    for state in game_state.next_states:
        assert state in player.game_states

def test_root_node_successors_in_player_game_graph_after_expansion(uct_player):
    _, root_node, player = uct_player
    player.game_graph.root_node.expand()
    for node in root_node.children:
        assert node in player.game_graph
