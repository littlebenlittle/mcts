
from mcts import GameState, GameOutcome


class NimState(GameState):

    __slots__ = ('_num_beads', '_player_turn',)

    def __init__(self, num_beads, player_turn):
        self._num_beads = num_beads
        assert player_turn in (1,2)
        self._player_turn = player_turn

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return  f'NimState({self.num_beads}, {self.player_turn})'
        # return f'<{__name__}.{self.__class__.__name__}' \
        #      + f'(num_beads={self.num_beads}, player_turn={self.player_turn})>'

    @property
    def player_turn(self):
        return self._player_turn

    @property
    def num_beads(self):
        return self._num_beads

    @property
    def is_terminal(self):
        return self.num_beads == 0

    @property
    def outcome(self):
        return NimOutcome(self)

    @property
    def next_states(self):
        assert not self.is_terminal
        for i in (1,2,3):
            num_beads = max(self.num_beads - i, 0)
            yield NimState(
                num_beads,
                1 if self.player_turn == 2 else 2,
            )

    def get_random_next_state(self):
        from random import choice
        n = choice(range(1, 4))
        return NimState(
            self.num_beads - n,
            1 if self.player_turn == 2 else 2,
        )


class NimOutcome(GameOutcome):

    __slots__ = ('_winner')

    def __init__(self, state):
        assert isinstance(state, NimState)
        assert state.num_beads == 0
        self._winner = 1 if state.player_turn == 2 else 2

    @property
    def winner(self):
        return self._winner
