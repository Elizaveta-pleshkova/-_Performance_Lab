import statistics
import sys
import argparse


def create_path_numbers():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='?')

    return parser


if __name__ == '__main__':
    parser = create_path_numbers()
    path_numbers = parser.parse_args()
    file_num = open(path_numbers.path, "rt")
    arr_file_num = file_num.readlines()
    file_num.close()

    arr_num = []
    for i in arr_file_num:
        arr_num.append(int(i))

    median = statistics.median_high(sorted(arr_num))

    count = 0
    for i in arr_num:
        while i != median:
            if i > median:
                i -= 1
                count += 1
            else:
                i += 1
                count += 1

    print(count)
