import numpy as np
from unittest import TestCase
from collections import defaultdict
import main as m


class TestAssign_points_to_centers(TestCase):
    def test_assign_points_to_centers(self):
        points = np.array([[.1, .1],
                             [.5, .5],
                             [.8, .8]])
        centers = np.array([[.11, .11],
                              [.51, .51],
                              [.81, .81]])

        answer = defaultdict(list)
        answer[0].append(np.array([.1, .1]))
        answer[1].append(np.array([.5, .5]))
        answer[2].append(np.array([.8, .8]))
        #np.testing.assert_array_equal(m.assign_points_to_centers(points, centers), answer, verbose=True)
        print m.assign_points_to_centers(points, centers)
        print answer
        print self.assertEqual(m.assign_points_to_centers(points, centers), answer)
        self.assertEqual(answer, answer)

        #defaultdict( < type'list' >, {0: [array([0.1, 0.1])], 1: [array([0.5, 0.5])], 2: [array([0.8, 0.8])]})
        #defaultdict( < type'list' >, {0: [array([0.1, 0.1])], 1: [array([0.5, 0.5])], 2: [array([0.8, 0.8])]})

