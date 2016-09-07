#
# k-means algorithm

import random
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict


def generate_points(number_of_points):
    return np.array([(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(number_of_points)])


def generate_points_gauss(number_of_points, number_of_clusters):
    n = float(number_of_points) / number_of_clusters
    result = []
    for i in range(number_of_clusters):
        c = (random.uniform(-1, 1), random.uniform(-1, 1))
        s = random.uniform(0.05, 0.5)
        x = []
        while len(x) < n:
            a, b = np.array([np.random.normal(c[0], s), np.random.normal(c[1], s)])
            if abs(a) < 1 and abs(b) < 1:
                x.append([a, b])
        result.extend(x)
    result = np.array(result)[:number_of_points]
    return result


def assign_points_to_centers(list_of_points, centers):
    clusters = defaultdict(list)
    for p in list_of_points:
        distances = []
        for c in centers:
            distances.append(np.linalg.norm(p - c))
        nearest_center = distances.index(min(distances))
        # print('point %s going to be friends with center %s') % (p, nearest_center)
        clusters[nearest_center].append(p)
    return clusters


def find_new_centers(clusters):
    new_centers = []
    for k in sorted(clusters.keys()):  # TODO remove sorted later
        new_centers.append(np.mean(clusters[k], axis=0))
    return np.array(new_centers)


def is_centers_match(cent, new_cent):
    return set([tuple(a) for a in cent]) == set([tuple(a) for a in new_cent])


def k_means(points, number_of_centers):
    centers = generate_points(number_of_centers)  # pick n random points
    clusters = assign_points_to_centers(points, centers)
    new_centers = find_new_centers(clusters)
    while not is_centers_match(centers, new_centers):
        centers = new_centers
        clusters = assign_points_to_centers(points, new_centers)
        new_centers = find_new_centers(clusters)
        draw_result(points, centers)
    return clusters, centers


def draw_result(board, centers):
    plt.plot(board[:, 0], board[:, 1], 'ro')
    plt.plot(centers[:, 0], centers[:, 1], 'bs', markersize=15)
    plt.show()


if __name__ == '__main__':
    no_of_centers = 3
    points = generate_points_gauss(number_of_points=9, number_of_clusters=no_of_centers)
    #clusters, centers = k_means(points, no_of_centers)
    print type(points)
    #draw_result(points, centers)

