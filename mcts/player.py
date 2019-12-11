
from types import SimpleNamespace
from mcts.node import GameNode

class UCTPlayer:

    def __init__(self, root_node):
        assert isinstance(root_node, GameNode)
        self._states = [root_node.game_state]
        self._graph = SimpleNamespace(
            root_node=root_node,
            nodes=[root_node],
        )

    @property
    def game_graph(self):
        return self._graph

    @property
    def game_states(self):
        return self._states

    def expand(self, node):
        assert isinstance(node, GameNode)
        node.expand()
        for s in node.successors:
            self._graph.nodes.append(s)
