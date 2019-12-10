
# Monte Carlo Tree Search

An opinionated framework for MCTS algorithms.

The guiding principle of this framework is extensibility. Operations that are too expensive to perform in the Python runtime can be outsourced via gRPC, HTTP/JSON, or Python's foreign function interface. As such, most properties return generators or iterators that can be evaluated as needed (lazy evaluation).

## TODOs

* Add unit tests
* Add docstrings
* Profile and add FFI bindings
* Change assert statements to meaningful errors

## Class Hierarchy

<!-- TODO: move this to sphinx docs? 2019-12-09T10:15:11Z -->

**mcts.GameState** Abstract base class for classes that represent the state of a game.

**games.NimState** represents the state of a game of Nim with a certain number of beads and player turn. `num_beads` can be any positive integer (zero included). `player_turn` can be either `1` or `2`.

**mcts.Player** Abstract base class for player data types.

**players.MCTSPlayer** Abstract base class for players that execute a MCTS algorithm with a `tree_policy` and `default_policy` as per [C. Browne](http://ccg.doc.gold.ac.uk/ccg_old/teaching/ludic_computing/ludic16.pdf).

**players.UCTPlayer** A MCTS player that implements UCB1 Algorithm for its `tree_policy` and uniform random play for its `default_policy`.

**mcts.GameTreeNode**
**mcts.Outcome**
