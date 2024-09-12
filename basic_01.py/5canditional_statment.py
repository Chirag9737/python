# they allows us to control the flow of the program
''' 
if
if - else
elif
ternary
switch
'''
#  1 light = input("light : ")

"""if light == "red" :
    print("Stop")
elif light == "blue" :
    print("Go")
elif light == "yellow ":
    print("look")
else  :
    print("light is demage")



#  2    marks =float(input("enter the marks : "))

if (marks >= 90) :
    print(" grade is : A")
elif (marks >= 80 and marks < 90 ):
    print("grade is : B")
elif (marks >= 70 and marks < 80) :
    print("grade is : C")
else  :
    print("grade is : D")"""


""" 3 number =  int(input("Enter a number : "))

if number >= 0 :
    print("num is positive")
else :
    print("num is nagetive")"""


#  4  even odd numbers program

"""num = int(input("enter a number : "))

if num % 2 == 0 :
    print("the num is a : Even")
else :
    print("the num is a : odd")"""


""" 5 cost_price = int(input("entr the cost price : "))
sell_price = int(input("entr the sell price : "))


if cost_price < sell_price :
    print("this product is : profiteble",sell_price - cost_price ,"rupis")
elif cost_price == sell_price :
    print("No loss : No profit")
else :
    print("this product is : lossable  ",cost_price - sell_price , "rupis")
"""

'''  num_1 = int(input('enter a num : '))
num_2 = int(input('enter a num : '))
num_3 = int(input('enter a num : '))

if num_1 > num_2 and num_1 > num_3 :
    print(num_1," is gretest number")
elif num_2 > num_3 and num_2 > num_1 :
    print(num_2, "is gretest number")
else :
    print(num_3, "is gretest number")'''

'''num_1 = int(input('enter a num : '))
num_2 = int(input('enter a num : '))
num_3 = int(input('enter a num : '))


if num_1 > num_2 :
    if num_1 > num_3 :
        print(num_1,"is gretest num")
    else :
        print(num_3,"is gretest num")
else :
    if num_2 > num_3:
        print(num_2,"is gretest num")
    else :
        print(num_3,"is gretest num")

'''

################# match case
num_1 = int(input("enter num 1 : "))
num_2 = int(input("enter num 2 : "))

operator = input("enter the opcode : ")
match  operator:
    case '+' :
        print(num_1 + num_2) 
    case '-' :
        print(num_1 - num_2) 
    case '*' :
        print(num_1 * num_2) 
    case '/' :
        print(num_1 / num_2) 
    case '//' :
        print(num_1 // num_2) 
    case '**' :
        print(num_1 ** num_2) 
    case _ :
        print("enter valide opcode")


#  ternary oprator

num = int(input("enrer the num : "))
print("O/P is a :","Even" if num % 2 == 0 else "Odd")
