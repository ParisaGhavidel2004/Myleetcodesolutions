# Love Calculator:
"""
1)2 value: Firstone write your name/ secondone write your Love name
2)True:       same words:
  t =4            l=1
  r =2            o=2
  u =1            v=0
  e =5            e=4
  sum:8           sum:7
so the score is:87

3)the score:
    less than 10 and graater than 90:"Your score is {x}, you go together like coke and metod"
    between 40 and 50: "Your score is {y}, you are alright together."
    Otherwise:"Your score is :{z}"
4)Use function lower() and count() in this program

"""
# My solution:::
name1 = input("What is your name? ")
name2 = input("What is your love name? ")
combined_string = name1+name2
lower_case_string = combined_string . lower()
t = lower_case_string . count("t")
r = lower_case_string . count("r")
u = lower_case_string . count("u")
e = lower_case_string . count("e")
true = t + r + u + e
l = lower_case_string . count("l")
o = lower_case_string . count("o")
v = lower_case_string . count("v")
e = lower_case_string . count("e")
love = l + o + v + e
loveScore = int(str(true) + str(love))
if (loveScore < 10 or loveScore > 90):
    print(f"Your score is {loveScore}, you go together like coke and metod")
elif 40 <= loveScore <= 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is :{loveScore}")

