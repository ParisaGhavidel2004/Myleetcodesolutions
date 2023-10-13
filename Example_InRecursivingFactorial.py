"""count a*b in this conditions:
a*b= 
    if b=1 ==> a
    if b>1 ==> a+a*(b-1)
use Recursive Function please
"""
def multiply(number1,number2):
    if number2 == 1:
        return number1
    elif number2>1:
        return number1+multiply(number1,number2-1)
    else:
        return "Please Entre a positive number :)"
 
a=int(input("Enter a : "))
b=int(input("Enter b: "))
print(multiply(a,b))