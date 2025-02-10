import pytest
import sys

from um import count

def test_count():
    assert count('um') == 1

def test_count2():
    assert count('um um') == 2

def test_count3():
    assert count('um um um') == 3

def test_count4():
    assert count('janl nflknas') == 0

def test_count5():
    assert count('umum to me') == 0

def test_count6():
    assert count('UM um wooo') == 2