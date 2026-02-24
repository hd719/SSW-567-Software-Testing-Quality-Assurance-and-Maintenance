"""Unit tests for triangle classification."""

import pytest

from main import classify_triangle


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (0, 1, 1, "invalid"),
        (-1, 2, 3, "invalid"),
        (1, 2, 3, "invalid"),
        (2, 2, 4, "invalid"),
    ],
)
def test_invalid_triangles(a, b, c, expected):
    """Validate detection of invalid triangles."""
    assert classify_triangle(a, b, c) == expected


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (3, 3, 3, "equilateral"),
        (3, 3, 2, "isosceles"),
        (3, 2, 3, "isosceles"),
        (2, 3, 3, "isosceles"),
        (4, 5, 6, "scalene"),
    ],
)
def test_basic_classifications(a, b, c, expected):
    """Validate equilateral, isosceles, and scalene classifications."""
    assert classify_triangle(a, b, c) == expected


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (3, 4, 5, "right scalene"),
        (5, 3, 4, "right scalene"),
        (6, 8, 10, "right scalene"),
    ],
)
def test_right_triangles(a, b, c, expected):
    """Validate right-triangle detection with side order variations."""
    assert classify_triangle(a, b, c) == expected
