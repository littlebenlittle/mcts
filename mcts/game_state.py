
class NimState:

    def __init__(self, num_beads, player_turn):
        if not isinstance(num_beads, int) or \
                num_beads < 0:
            raise ValueError
        if not player_turn in (1, 2):
            raise ValueError
        self._num_beads = num_beads
        self._player_turn = player_turn

    @property
    def next_states(self):
        return [
            NimState(24, 2),
            NimState(23, 2),
            NimState(22, 2),
        ]

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self._num_beads == other._num_beads \
                and self._player_turn == other._player_turn
