def rfib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return rfib(n-1) + rfib(n-2)

