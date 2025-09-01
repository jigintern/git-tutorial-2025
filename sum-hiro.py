def sum(a, b):
    return a + b
def abDef(a, b):
    return abs(a - b)
def mul(a, b):
    return a * b

A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
print("The sum is:", sum(A, B))
print("The absolute difference is:", abDef(A, B))
print("The multiply is:", mul(A, B))