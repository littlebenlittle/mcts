
class GameNode:

    def __init__(self, game_state):
        self._state = game_state

    def expand(self):
        pass

    @property
    def children(self):
        return list()

    @property
    def game_state(self):
        return self._state
