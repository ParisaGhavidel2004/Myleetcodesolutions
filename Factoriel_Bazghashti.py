""" counting Factorial whith recursive function(Bazghashti)"""
def Rfactoial(anumber):
    factorial=1
    if anumber==1 or anumber==0 :
        return factorial
    else:
        return anumber * Rfactoial(anumber-1)


number=int(input("Enter the number to calculate Factorial of that number: "))
print("the answer is: ", Rfactoial(number))


