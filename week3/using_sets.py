# numbers_set = {1, 2, 3, 4, 4}       # duplicate values removed, can't have duplicates in a set
# numbers_set = {1, 2, 3, 4, [5, 6]}    # can't use mutable data types
# numbers_set = {1, 2, 3, 4, (5, 6)}    # tuples are immutable, OK to use!
# print(numbers_set)

words_set = {"Alpha", "Bravo", "Charlie"}
""" abcd = ""
for word in words_set:
    abcd += word
print(abcd) """
""" if "Alpha" in words_set:
    print("Alpha is in set")
else:
    print("Alpha not in set") """

words_set.add("Delta")
print(words_set)
words_set.discard("Bravo")
print(words_set)
