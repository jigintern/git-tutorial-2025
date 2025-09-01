import random

A, B = random.randint(1,100), random.randint(1,100)
C = str(int(A) + int(B))
A, B = str(A), str(B)

print("sum " + A + " plus " + B + " equals " + C)