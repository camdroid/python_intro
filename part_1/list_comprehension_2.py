# Building the set S = {x^2: x in {0..9} if x is even}

# No LC
S1 = []
for x in range(10):
    if x % 2 == 0:
        S1.append(x**2)

# Using LC
S2 = [x**2 for x in range(10) if x % 2 == 0]

print(S1)
print(S2)
