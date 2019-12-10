
import util
from abc import abstractmethod
from mcts import Player, GameTreeNode

import logging
logging.basicConfig(level=logging.DEBUG)

class MCTSPlayer(Player):

    def __init__(self):
        super().__init__()
        self._stats = dict()
        self._root_node = None

    def choose(self, state, max_rollouts=1000):
        assert not state.is_terminal
        self._root_node = self.node_from_state(state)
        num_rollouts = 0
        for _ in range(100):
            current = self._root_node
            while current.is_expanded:
                current = self.tree_policy(current)
            if current.is_terminal:
                continue
            if self._stats[current].num_visits == 0:
                self.do_rollout(current)
            else:
                self._expand(current)
        return self._select()

    def _expand(self, node):
        assert not node.is_expanded
        if node.is_terminal:
            raise ValueError(f'{node} is terminal')
        node.expand()
        for child in node.children:
            self._register_node(child)

    def _register_node(self, node):
        from types import SimpleNamespace
        super()._register_node(node)
        self._stats[node] = SimpleNamespace(
            num_visits=0,
            sum_utility=0,
        )

    @abstractmethod
    def tree_policy(self, node):
        pass

    @abstractmethod
    def default_policy(self, node):
        pass

    @abstractmethod
    def do_rollout(self, node):
        pass

    @abstractmethod
    def _select(self):
        pass

    @abstractmethod
    def backpropogate(self, node, utility):
        pass


class UCTPlayer(MCTSPlayer):

    def __init__(self, utility_fn, max_child_samples=10):
        super().__init__()
        self._max_child_samples = max_child_samples
        self.utility = utility_fn

    def ucb1(self, node):
        assert isinstance(node, GameTreeNode)
        assert node in self._stats
        assert node.parent in self._stats
        from math import sqrt, log
        n = self._stats[node].num_visits
        if n == 0:
            return float('inf')
        u = self._stats[node].sum_utility
        N = self._stats[node.parent].num_visits
        return u/n + sqrt(log(N)/n)

    def tree_policy(self, node):
        assert isinstance(node, GameTreeNode)
        if node.is_terminal:
            utility = self.utility(node.state.outcome)
            self.backpropogate(node, utility)
            return self._root_node
        return max(node.children, key=self.ucb1)

    def default_policy(self, node):
        assert isinstance(node, GameTreeNode)
        from random import choice
        a = util.getn(
            self._max_child_samples,
            node.state.next_states
        )
        return self.node_from_state(choice(a))

    def do_rollout(self, node):
        assert isinstance(node, GameTreeNode)
        current = node
        while not current.is_terminal:
            current = self.default_policy(current)
        utility = self.utility(current.state.outcome)
        self.backpropogate(node, utility)

    def backpropogate(self, node, utility):
        self._stats[node].num_visits += 1
        self._stats[node].sum_utility += utility
        if not node.is_root:
            self.backpropogate(node.parent, -utility)

    def _select(self):
        max_ = 0
        argmax_ = None
        for state, node in self._nodes.items():
            if node.is_root:
                continue
            num_visits = self._stats[node].num_visits 
            if num_visits > max_:
                max_ = num_visits
                argmax_ = state
        return argmax_
