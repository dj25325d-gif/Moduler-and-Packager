import math


def factorial(n):

    return math.factorial(n)


def compound_interest(p, r, t):

    return round(p * (1 + r/100) ** t, 2)


def trig(angle):

    rad = math.radians(angle)

    return math.sin(rad), math.cos(rad), math.tan(rad)


def circle_area(r):

    return math.pi * r * r


def rectangle_area(l, w):

    return l * w


def triangle_area(b, h):

    return 0.5 * b * h
