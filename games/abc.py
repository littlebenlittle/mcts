
from abc import ABC, abstractproperty, abstractmethod
from games.util import UUIDHash
from games.exceptions import WrongPlayer


class Game(ABC):
    @abstractproperty
    def current_state(self):
        pass

    @abstractproperty
    def current_player(self):
        pass

class AlternatingTwoPlayerGame(Game):
    ''' A two-player game in which players take alternating turns '''

    def __init__(self, player1, player2):
        self._p1 = player1
        self._p2 = player2
        self._current_player = self._p1

    def make_move(self, player, move):
        if self._current_player != player:
            raise WrongPlayer()
        self._make_move(player, move)
        if self._current_player == self._p1:
            self._current_player = self._p2
        else:
            self._current_player = self._p1

    @property
    def current_player(self):
        return self._current_player

    @abstractmethod
    def _make_move(self, player, move):
        pass

class GameMove(ABC):
    pass

class GameState(ABC):
    pass

class Player(ABC):
    @abstractmethod
    def play(self, game):
        '''Make a choice and play one step of the game'''
        pass


class UUIDPlayer(Player, UUIDHash):
    def __init__(self):
        super().__init__()
