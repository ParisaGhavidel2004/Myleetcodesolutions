"""a+b with recursive function: """


def Sum(num1, num2):
    if num2 == 0:
        return num1
    return Sum(num1, num2-1) + 1


a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
print("Sum of num(a) & num(b) is: ", Sum(a, b))
