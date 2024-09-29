def linear_search_dictionary(dict, target):
    for x in dict:  # search each value in dictionary
        if dict[x] == target:   # compare value with target value
            print(f"Found at key {x}")  # if value matches target
            return x
    print("Target is not in the dictionary")    # if target is not in dictionary
    return -1


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)

