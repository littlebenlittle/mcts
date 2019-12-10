
from abc import ABC, abstractproperty, abstractmethod


class GameState(ABC):

    @abstractproperty
    def next_states(self):
        pass

    @abstractproperty
    def is_terminal(self):
        pass

    @abstractproperty
    def outcome(self):
        pass


class GameOutcome(ABC):
    pass


class GameTreeNode:

    __slots__ = ('_state', '_parent', '_children', '_is_expanded',)

    def __init__(self, state, parent=None):
        assert isinstance(state, GameState)
        assert parent is None or isinstance(parent, GameTreeNode)
        self._state = state
        self._parent = parent
        self._is_expanded = False
        self._children = None

    def __repr__(self):
        return f'<{__name__}.{self.__class__.__name__}' \
             + f'(state={self.state}>'

    @property
    def state(self):
        return self._state

    @property
    def parent(self):
        return self._parent

    @property
    def is_expanded(self):
        return self._is_expanded

    @property
    def is_root(self):
        return self.parent is None

    @property
    def root(self):
        if self.is_root:
            return self
        return self.parent.root

    @property
    def is_terminal(self):
        return self.state.is_terminal

    @property
    def children(self):
        assert self.is_expanded
        for c in self._children:
            yield c
        
    def expand(self):
        assert not self.is_expanded
        self._is_expanded = True
        self._children = list()
        for state in self.state.next_states:
            self._children.append(GameTreeNode(state, parent=self))


class Player(ABC):

    __slots__ = ('_nodes',)

    def __init__(self):
        self._nodes = dict()

    def node_from_state(self, state):
        assert isinstance(state, GameState)
        if state in self._nodes.keys():
            return self._nodes[state]
        node = GameTreeNode(state)
        self._register_node(node)
        return node

    def state_from_node(self, node):
        return node.state

    def _register_node(self, node):
        assert isinstance(node, GameTreeNode)
        assert not self._is_registered(node.state)
        self._nodes[node.state] = node

    def _is_registered(self, node):
        return node in self._nodes.values()

    @abstractmethod
    def choose(self, state):
        pass
