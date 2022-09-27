import unittest
import numpy as np
from src.section2_geometry import Plane


class MyTestCase(unittest.TestCase):
    def test_Q2_parameters(self):
        my_plane = Plane(n=np.asarray([0, 0, 1]), origin=np.asarray([0, 0, 0]))
        parameters = my_plane.get_parameters()
        self.assertTrue(np.all(parameters == (0, 0, 1, 0)), "wrong parameters")

        my_plane = Plane(n=np.asarray([0, 0, 100]), origin=np.asarray([0, 0, 0]))
        parameters = my_plane.get_parameters()
        self.assertTrue(np.all(parameters == (0, 0, 1, 0)), "wrong parameters")

    def test_Q2_distance(self):
        my_plane = Plane(n=np.asarray([0, 0, 1]), origin=np.asarray([0, 0, 0]))
        d = my_plane.compute_distance(np.array([0, 5, 5]))
        self.assertEqual(d, 5, "distance from plane should be 5")
        d = my_plane.compute_distance(np.array([0, 5, -5]))
        self.assertEqual(d, -5, "distance from plane should be -5")
        d = my_plane.compute_distance(np.array([0, 5, 0]))
        self.assertEqual(d, 0, "distance from plane should be 0")


if __name__ == '__main__':
    unittest.main()
