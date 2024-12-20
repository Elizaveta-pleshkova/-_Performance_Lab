from itertools import cycle
import sys
import argparse


def create_path_numbers():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', nargs='?')
    parser.add_argument('m', nargs='?')

    return parser


if __name__ == '__main__':
    parser = create_path_numbers()
    numbers = parser.parse_args()
    n = int(numbers.n)
    m = int(numbers.m)

    array = []

    for i in range(n):
        array.append(i + 1)

    circular_array = cycle(array)

    full_intervals = []
    last_elem = 0
    new_m = m

    while last_elem != array[0]:
        interval = []
        if last_elem != 0:
            interval.append(last_elem)
            new_m = m - 1
        for i in range(new_m):
            last_elem = next(circular_array)
            interval.append(last_elem)
        full_intervals.append(interval)

    resulting_path = []
    for i in full_intervals:
        resulting_path.append(str(i[0]))

    print("".join(resulting_path))
