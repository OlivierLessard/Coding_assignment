import unittest
import numpy as np
from src.section1_geometry import Q1_find_line, Q2_find_intersection


class MyTestCase(unittest.TestCase):
    def test_Q1_passing_through(self):
        p1 = np.array([2, 3])
        p2 = np.array([6, -5])
        a, b = Q1_find_line(p1, p2)
        self.assertEqual(p1[1], a * p1[0] + b, "line not passing throught the point")
        self.assertEqual(p2[1], a * p2[0] + b, "line not passing throught the point")
        p2 = np.array([2, 3])
        p1 = np.array([6, -5])
        a, b = Q1_find_line(p1, p2)
        self.assertEqual(p1[1], a * p1[0] + b, "line not passing throught the point")
        self.assertEqual(p2[1], a * p2[0] + b, "line not passing throught the point")

    def test_Q1_same_point(self):
        p1 = np.array([2, 3])
        p2 = p1

        with self.assertRaises(Exception) as context:
            Q1_find_line(p1, p2)
        self.assertTrue("p1 and p2 are the same point" in str(context.exception))

    def test_Q2_find_intersection(self):
        a1, b1, c1 = 1, -2, 1
        a2, b2, c2 = 1, -3, -3
        x0, y0 = Q2_find_intersection(a1, b1, c1, a2, b2, c2)
        self.assertEqual(0, a1*x0+b1*y0+c1, "intersection is not on the 1rst line")
        self.assertEqual(0, a2*x0+b2*y0+c2, "intersection is not on the 2nd line")

    def test_Q2_parallel(self):
        a1, b1, c1 = 1, -2, 1
        a2, b2, c2 = 1, -2, -3
        with self.assertRaises(Exception) as context:
            Q2_find_intersection(a1, b1, c1, a2, b2, c2)
        self.assertTrue("they are parallel lines" in str(context.exception))

    def test_Q2_same(self):
        a1, b1, c1 = 1, -2, 1
        a2, b2, c2 = 1, -2, 1
        with self.assertRaises(Exception) as context:
            Q2_find_intersection(a1, b1, c1, a2, b2, c2)
        self.assertTrue("they are identical lines" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
