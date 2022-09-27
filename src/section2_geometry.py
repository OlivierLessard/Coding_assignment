import numpy as np


class Plane:
    def __init__(self, n, origin):
        self.n = n / ((n ** 2).sum() ** 0.5)    # [a, b, c]
        self.origin = origin                    # [x0, y0, z0]

    def get_parameters(self):
        d = -self.n[0] * self.origin[0] - self.n[1] * self.origin[1] - self.n[2] * self.origin[2]
        return self.n[0], self.n[1], self.n[2], d

    def compute_distance(self, point):
        # positive if the point is on the same side as the normal
        distance = (self.n[0] * point[0] + self.n[1] * point[1] + self.n[2] * point[2] + self.get_parameters()[3]) / \
                   (np.sqrt(np.sum(self.n ** 2)))
        return distance
