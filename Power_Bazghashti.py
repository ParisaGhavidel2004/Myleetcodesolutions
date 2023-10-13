"""counting a power b with Recusive functionf: """


def my_power(number1, number2):
    if number2 == 1:
        return number1
    return number1 * my_power(number1, number2-1)


a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("The answer is:", my_power(a, b))
