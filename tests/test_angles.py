import pytest
from mathlib.angles import deg2rad, rad2deg, normalize_deg

def test_deg2rad():
    assert math.isclose(deg2rad(0), 0)
    assert math.isclose(deg2rad(180), math.pi)
    assert math.isclose(deg2rad(360), 2 * math.pi)

def test_rad2deg():
    assert math.isclose(rad2deg(0), 0)
    assert math.isclose(rad2deg(math.pi), 180)
    assert math.isclose(rad2deg(2 * math.pi), 360)

def test_normalize_deg():
    assert normalize_deg(360) == 0
    assert normalize_deg(400) == 40
    assert normalize_deg(-10) == 350
