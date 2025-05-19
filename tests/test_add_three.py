import pytest

from olly_demo.example import add_three, add_two

def test_add_three():
    assert add_three(1, 2) == 5

def test_add_two():
    assert add_two(1, 2)== 5
