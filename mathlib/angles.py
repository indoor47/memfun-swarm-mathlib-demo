import math

def deg2rad(degrees: float) -> float:
    return math.radians(degrees)

def rad2deg(radians: float) -> float:
    return math.degrees(radians)

def normalize_deg(degrees: float) -> float:
    return degrees % 360
