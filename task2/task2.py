import math

file1 = open("circle.txt", "rt")
arr_file1 = file1.readlines()
file1.close()

file2 = open("dot.txt", "rt")
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
    print(t1, t2)
    hypotenuse = math.sqrt((t1 - kc1) ** 2 + (t2 - kc2) ** 2)
    if hypotenuse == r:
        print(0)
    elif hypotenuse < r:
        print(1)
    else:
        print(2)
