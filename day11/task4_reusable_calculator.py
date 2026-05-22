def add(a, b):
    return a +b

def subtract(a, b):
    return a- b

def multiply(a, b):
    return a* b

def divide(a, b):
    if b==0:
        return "Error : Division by zero"
    return a/b

num1 =float(input("enter first number: "))
num2 =float(input("enter second number:"))

print(f"Addition:{add(num1,num2)}")
print(f"subtraction: {subtract(num1, num2)}")
print(f"multiply:{multiply(num1,num2)}")
print(f"division:{divide(num1,num2)}")

