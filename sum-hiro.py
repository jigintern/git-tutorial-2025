def sum(a, b):
    return a + b
def min(a, b):
    return abs(a - b)

A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
print("The sum is:", sum(A, B))
print("The absolute difference is:", min(A, B))