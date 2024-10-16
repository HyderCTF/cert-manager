"""
Unit tests for calc module.
"""

import pytest
from calc import add, subtract

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    """Test for the add function."""
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),
    (2, 3, -1),
    (0, 0, 0)
])
def test_subtract(a, b, expected):
    """Test for the subtract function."""
    assert subtract(a, b) == expected
