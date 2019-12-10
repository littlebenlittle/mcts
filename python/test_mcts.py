
from games import NimState
from players import UCTPlayer


def nim_utility(outcome):
    if outcome.winner == 1:
        return 1
    return -1


def test_mcts():
    init_state = NimState(25, 1)
    p = UCTPlayer(nim_utility)
    for _ in range(100):
        choice = p.choose(init_state)
        print(choice)
        assert choice in list(init_state.next_states)
    assert False
