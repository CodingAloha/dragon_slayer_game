import timeit

print(timeit.timeit("[x for x in range(1000000)]", number=1))
print(timeit.timeit("[x for x in range(10000000)]", number=1))
print(timeit.timeit("[x for x in range(100000000)]", number=1))
