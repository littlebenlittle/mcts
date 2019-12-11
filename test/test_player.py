
from mcts.node import NotExpanded
import pytest

@pytest.fixture
def uct_player():
    from mcts.player import UCTPlayer
    from mcts.node import GameNode
    from mcts.game_state import NimState
    game_state = NimState(25, 1)
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

def test_root_node_is_not_expanded_before_expansion(uct_player):
    _, root_node, player = uct_player
    assert not root_node.is_expanded

def test_root_node_is__expanded_after_expansion(uct_player):
    _, root_node, _ = uct_player
    root_node.expand()
    assert root_node.is_expanded

def test_root_node_successors_raises_if_called_before_expansion(uct_player):
    _, root_node, _ = uct_player
    with pytest.raises(NotExpanded):
        root_node.successors

def test_root_node_has_successors_after_expansion(uct_player):
    _, root_node, _ = uct_player
    root_node.expand()
    assert len(root_node.successors) == 3

def test_nim_state_init_with_negative_beads():
    from mcts.game_state import NimState
    with pytest.raises(ValueError):
        NimState(-1, 1)

def test_nim_state_init_with_float_beads():
    from mcts.game_state import NimState
    with pytest.raises(ValueError):
        NimState(1.0, 1)

def test_nim_state_init_with_unknown_player():
    from mcts.game_state import NimState
    with pytest.raises(ValueError):
        NimState(3, 0)

def test_nim_state_init():
    from mcts.game_state import NimState
    with pytest.raises(ValueError):
        NimState(3, 3)

def test_nim_state_relations():
    from mcts.game_state import NimState
    assert NimState(25, 1) == NimState(25, 1)
    assert NimState(25, 1) != NimState(24, 1)
    assert NimState(25, 1) != NimState(25, 2)

def test_game_state_next_states(uct_player):
    game_state, _, _ = uct_player
    from mcts.game_state import NimState
    assert NimState(24, 2) in game_state.next_states
    assert NimState(23, 2) in game_state.next_states
    assert NimState(22, 2) in game_state.next_states

def test_root_node_successors_type(uct_player):
    from mcts.node import GameNode
    _, root_node, _ = uct_player
    root_node.expand()
    for node in root_node.successors:
        assert isinstance(node, GameNode)

def test_game_state_next_states_not_in_player_game_states_before_expansion(uct_player):
    game_state, _, player = uct_player
    for state in game_state.next_states:
        assert not state in player.game_states

def test_root_node_successors_in_player_game_graph_after_expansion(uct_player):
    _, root_node, player = uct_player
    player.expand(root_node)
    for node in root_node.successors:
        assert node in player.game_graph.nodes
