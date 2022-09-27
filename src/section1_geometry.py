import numpy as np


def Q1_find_line(p1, p2):
    """
    returns the paramater a and b of the line (y = ax+b) passing through those points
    :param p1: numpy array [x0, y0]
    :param p2: numpy array [x1, y1]
    :return: integers a and b
    """
    assert np.any(p1 != p2), "p1 and p2 are the same point"
    a = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = -a * p1[0] + p1[1]
    return a, b


def Q2_find_intersection(a1, b1, c1, a2, b2, c2):
    """
    return the intersection point of two lines in 2D
    :param a1: float, parameter in a1*x + b1*y + c1 = 0
    :param b1: float, parameter in a1*x + b1*y + c1 = 0
    :param c1: float, parameter in a1*x + b1*y + c1 = 0
    :param a2: float, parameter in a2*x + b2*y + c2 = 0
    :param b2: float, parameter in a2*x + b2*y + c2 = 0
    :param c2: float, parameter in a2*x + b2*y + c2 = 0
    :return: floats x0, y0
    """
    parallel = True if a1 / b1 == a2 / b2 else False
    same = True if (parallel and c1 == c2) else False
    assert not same, "the two lines don't have a single intersection point, they are identical lines"
    assert not parallel, "the two lines don't have a single intersection point, they are parallel lines"

    return (b1*c2-b2*c1)/(a1*b2-a2*b1), (c1*a2-c2*a1)/(a1*b2-a2*b1)
