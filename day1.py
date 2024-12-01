import numpy as np
from IPython import embed

def get_distance(file):
    with open(file) as f:
        lines = f.readlines()
        left_side = np.sort(np.array([int(line.split()[0]) for line in lines]))
        right_side = np.sort(np.array([int(line.split()[1]) for line in lines]))
        distances = np.abs(right_side - left_side)

        return distances.sum()


def get_similarity(file):
    with open(file) as f:
        lines = f.readlines()
        left_side = np.array([int(line.split()[0]) for line in lines])
        right_side = np.array([int(line.split()[1]) for line in lines])

        counts = []
        for i in left_side:
            count = (right_side == i).sum()
            counts.append(count)
        counts = np.array(counts)

        similarities = left_side * counts
        return similarities.sum()


print(get_distance("inputs/day1.txt"))
print(get_similarity("inputs/day1.txt"))