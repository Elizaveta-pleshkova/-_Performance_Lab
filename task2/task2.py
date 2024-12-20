import math
import sys
import argparse


def create_path_numbers():
    parser = argparse.ArgumentParser()
    parser.add_argument('circle', nargs='?')
    parser.add_argument('dot', nargs='?')

    return parser


if __name__ == '__main__':
    parser = create_path_numbers()
    data = parser.parse_args()
    file1 = open(data.circle, "rt")
    arr_file1 = file1.readlines()
    file1.close()

    file2 = open(data.dot, "rt")
    arr_file2 = file2.readlines()
    file1.close()

    for i in range(len(arr_file1)):
        string = arr_file1[i].split()
        if i == 0:
            kc1 = float(string[0])
            kc2 = float(string[1])
        else:
            r = float(string[0])

    for i in range(len(arr_file2)):
        string = arr_file2[i].split()
        t1 = float(string[0])
        t2 = float(string[1])
        hypotenuse = math.sqrt((t1 - kc1) ** 2 + (t2 - kc2) ** 2)
        if hypotenuse == r:
            print(0)
        elif hypotenuse < r:
            print(1)
        else:
            print(2)
