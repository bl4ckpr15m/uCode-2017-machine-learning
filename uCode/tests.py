import pytest
from uCode import tasks as _


def test_dummy():
    assert _.dummy_plus(5, 9) == 14
