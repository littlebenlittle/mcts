
class NotExpanded(Exception):
    pass

class GameNode:

    def __init__(self, game_state):
        self._state = game_state
        self._successors = list()
        self._is_expanded = False

    def expand(self):
        for state in self.game_state.next_states:
            node = GameNode(state)
            self._successors.append(node)
        self._is_expanded = True

    @property
    def successors(self):
        if not self.is_expanded:
            raise NotExpanded
        return self._successors

    @property
    def game_state(self):
        return self._state

    @property
    def is_expanded(self):
        return self._is_expanded
