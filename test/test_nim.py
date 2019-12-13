
import pytest
from games.nim import Nim, NimState, ConstantNimPlayer
from games.exceptions import WrongPlayer

@pytest.fixture
def initialized_nim():
    p1 = ConstantNimPlayer(1)
    p2 = ConstantNimPlayer(3)
    g = Nim(25, p1, p2)
    return p1, p2, g

def test_NimState_is_terminal():
    assert NimState(0,1).is_terminal

def test_NimState_is_not_terminal():
    assert not NimState(3,2).is_terminal

def test_NimState_equality1():
    assert NimState(25,1) == NimState(25,1)

def test_NimState_equality2():
    assert NimState(27,2) == NimState(27,2)

def test_NimState_inequality1():
    assert not NimState(23,1) == NimState(25,1)

def test_NimState_inequality2():
    assert not NimState(25,2) == NimState(25,1)

def test_NimState_negative_beads():
    with pytest.raises(ValueError):
        NimState(-3,1)

def test_NimState_hash_equality1():
    assert hash(NimState(25,1)) == hash(NimState(25,1))

def test_NimState_hash_equality2():
    assert hash(NimState(27,2)) == hash(NimState(27,2))

def test_NimState_hash_inequality1():
    assert not hash(NimState(23,1)) == hash(NimState(25,1))

def test_NimState_hash_inequality2():
    assert not hash(NimState(25,2)) == hash(NimState(25,1))

def test_NimState_negative_beads():
    with pytest.raises(ValueError):
        NimState(-3,1)

def test_NimState_invalid_player():
    with pytest.raises(ValueError):
        NimState(0,0)

def test_Nim_initial_state(initialized_nim):
    p1, p2, g = initialized_nim
    assert g.current_state == NimState(25, 1)
