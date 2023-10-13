"""counting 1 to n with recusive function: """
def sum(number):
    if number == 1:
        return number
    return number + sum(number-1)


N = int(input("Enter N please, to counting sum of 1 to N: "))
print("The sum is: ",sum(N))
