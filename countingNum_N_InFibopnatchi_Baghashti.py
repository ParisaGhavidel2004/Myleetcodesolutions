"""acounting number n in Fibonatchi with recursive function: """


def Fibo(anumber):
    if anumber == 1 or anumber == 2:
        return 1
    if anumber > 2:
        return Fibo(anumber-1) + Fibo(anumber-2)


number = int(input("calculating Fibonatchi, Enter a num: "))
print("The answer is: ", Fibo(number))
