# check leap year(sale Kabise)
"""
It has a FlowChart in google
"""
user_year=int(input("Enter year to check that it is leap or not: "))
if user_year % 4 == 0 :
    if user_year % 100 ==0: 
        if user_year % 400 == 0:
            print("leap")
        else:
            print("Not leap")
    else: 
        print("leap")
else:
    print("Not leap")