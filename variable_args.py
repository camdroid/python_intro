def add(*args):
    sum = 0
    for a in args:
        sum += a
    return sum

print(add(3, 5))
# Prints 8

print(add(1, 2, 3, 4))
# Prints 10
