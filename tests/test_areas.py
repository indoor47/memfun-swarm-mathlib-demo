import pytest
from mathlib.areas import rectangle_area, circle_area, triangle_area

def test_rectangle_area():
    assert rectangle_area(3, 4) == 12
    assert rectangle_area(5, 5) == 25

def test_circle_area():
    assert math.isclose(circle_area(1), math.pi)
    assert math.isclose(circle_area(2), 4 * math.pi)

def test_triangle_area():
    assert triangle_area(10, 5) == 25
    assert triangle_area(7, 3) == 10.5
