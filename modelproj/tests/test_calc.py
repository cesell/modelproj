""" Test Cases for calc.py
"""

from modpro import calc


def test_add():
    result = calc.sum(4, 5)
    assert result == 9


def test_mul():
    result = calc.mul(10, 3)
    assert result == 30


def test_concat():
    assert calc.mul('a', 3) == 'aaa'
