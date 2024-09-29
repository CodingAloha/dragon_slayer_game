def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]

        if pivot_value == target:
            return pivot
        if pivot_value > target:
            upper_bound = pivot - 1
        else:
            lower_bound = pivot + 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, 10))
print(binary_search(my_list, 4))
print(binary_search(my_list, 33))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list.index(4))
''' Output:
            3   # index 3 contains the value 4
'''