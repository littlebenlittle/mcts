
from games.abc import AlternatingTwoPlayerGame, GameState, UUIDPlayer, GameMove
from games.exceptions import WrongPlayer


class Nim(AlternatingTwoPlayerGame):

    def __init__(self, starting_beads, player1, player2):
        super().__init__(player1, player2)
        self._current_state = NimState(starting_beads,1)

    @property
    def current_state(self):
        return self._current_state

    @property
    def current_player(self):
        return self._current_player

    @property
    def choices(self):
        hi = max(4, self.current_state.beads + 1)
        for i in range(0, hi):
            yield NimMove(i)

    def _make_move(self, player, move):
        assert isinstance(move, NimMove)
        assert isinstance(player, UUIDPlayer)
        if player != self.current_player:
            raise WrongPlayer()
        beads = self.current_state.beads - move.n
        if self.current_player == self._p1:
            self._current_state = NimState(beads, 2)
            self._current_player = self._p2
        if self.current_player == self._p2:
            self._current_state = NimState(beads, 1)
            self._current_player = self._p1


class NimMove(GameMove):

    def __init__(self, n):
        '''Take away n beads'''
        self._n = n

    @property
    def n(self):
        return self._n


class NimState(GameState):

    def __init__(self, beads, player):
        if not isinstance(beads, int) or beads < 0:
            raise ValueError(f'NimState.beads must be positive int; got {beads}')
        if player not in (1,2):
            raise ValueError(f'NimState.player must be 1 or 2; got {player}')
        self._beads = beads
        self._player = player
    
    @property
    def beads(self):
        return self._beads

    @property
    def player(self):
        return self._player

    @property
    def is_terminal(self):
        return self.beads == 0

    def __repr__(self):
        return f'NimState({self.beads},{self.player})'

    def __eq__(self, other):
        return self.beads == other.beads and self.player == other.player

    def __hash__(self):
        return hash((self.__class__.__name__, self.beads, self.player))


class ConstantNimPlayer(UUIDPlayer):

    def __init__(self, n):
        '''A player that always takes a fixed number n of beads'''
        super().__init__()
        self._n = n

    def play(self, game):
        assert isinstance(game, Nim)
        move = NimMove(self._n)
        game.make_move(self, move)
