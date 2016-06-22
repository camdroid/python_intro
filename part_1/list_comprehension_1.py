# Building the set S = {x^2: x in {0..9}}

# The non-LC way
S1 = []
for x in range(10):
    S1.append(x**2)

# The Pythonic way (using LC)
S2 = [x**2 for x in range(10)]

print(S1)
print(S2)
