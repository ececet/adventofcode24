import numpy as np


def get_inputs(file):
    with open(file) as f:
        lines = f.readlines()
        lines = [line.split() for line in lines]
        lines_int = []

        for line in lines:
            line = np.array([int(i) for i in line])
            lines_int.append(line)

        return lines_int


def remove_and_validate(row):
    for i in range(len(row)):
        row_copy = row.copy()
        row_copy = np.delete(row_copy, i)
        if validate_row(row_copy):
            return True
    return False


def is_decreasing(row):
    # Check if all consecutive numbers decrease
    return np.all(row[1:] < row[:-1])


def is_increasing(row):
    # Check if all consecutive numbers increase
    return np.all(row[1:] > row[:-1])


def diff_ok(row):
    # Check if all consecutive numbers increase or decrease by at most 2
    diff = np.abs(row[1:] - row[:-1])
    return np.all(diff <= 3)


def validate_row(row):
    if diff_ok(row) and is_decreasing(row):
        return True
    if diff_ok(row) and is_increasing(row):
        return True
    return False


def main():
    inputs = get_inputs("inputs/day2.txt")
    validated = 0

    for row in inputs:
        if validate_row(row):
            validated += 1
            continue

        if remove_and_validate(row):
            validated += 1

    return validated

print(main())