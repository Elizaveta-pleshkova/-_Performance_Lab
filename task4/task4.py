import statistics

path_numbers = input("Enter the default path of the Numbers file: ")
file_num = open(path_numbers, "rt")
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
