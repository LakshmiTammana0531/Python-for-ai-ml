#conditional: if, if-else, if-elif-else

######### using if statement
x = int(input("enter the value of x:")) 
y = int(input("enter the value of y:")) 
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")    
if x==y:
    print("x is equal to y") 

#check whether the given number 
num =  int(input("enter the number:"))
if num%2 == 0:
    print("the number is even")
else:
    print("the number is odd") 

age = int(input("enter the age to check eligibility:"))
if age >= 18 :
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

if marks==90 and marks==80 :
    print("grade A")
else:
    print("fail")


######### using if-else:
age= int(input("age:"))
if(age >= 18):
    print("you are eligible")
else:
    print("you are not eligible!!")

a =int(input("enter the first number"))
b =int(input("enter the second number"))
if(a>b):
    print("first number is greater than next number")
else:
    print("first number is smaller than next number")

num = int(input("enter the number to know whether it is even or not:"))
if num%2 == 0:
    print("the number is even")
else:
    print("the number is odd")

num = int(input("enter the number to know whether it is positive or negative:"))
if num>0:
    print("the number is positive")
else:
    print("the number is negative")


######## using if-elif-else (ladder):

first = input("Enter the first number:")
operator = input("Enter the operator number(+,-,*,/,%) : ")
second = input("Enter the second number:")
first =int(first)
second =int(second)
if operator =="+": 
    print(first + second)
elif operator =="-": 
    print(first - second)
elif operator =="*": 
    print(first * second)
elif operator =="/": 
    print(first / second)
elif operator =="%": 
    print(first % second)
else:
    print("Invalid operation")


temp = int(input("Enter the temperature:"))
if temp<0:
    print("the temperature is freezing wearther.")
elif 0<temp<10:
    print("The temperature is very cold.")
elif 10<temp<20:
    print("The temperature is cold. ")
elif 20<temp<30:
    print("The temperature is Normal.")
elif 30<temp<40:
    print("The temperature is Hot.")
else:
    print("The temperature is very Hot")


x = int(input("enter the value of x:")) 
y = int(input("enter the value of y:")) 
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")    
else :
    print("x is equal to y") 


marks = int(input("enter the marks:"))
if 90 <= marks :
    print("grade A")
elif 75<marks<90  :
    print("grade B")
elif 45<marks<75 :
    print ("grade C")
elif marks < 45 :
    print(" grade D")

age=int(input("enter the age :"))
time=int(input("Enter the time in 24-hrs format:"))
price = 0
if age<12:
    price=8.00
    print("The price of ticket is :$",price)
elif age>=65:
    price=7.00
    print("The price of ticket is :$",price)
else:
    price=12.00
    print("The price of ticket is:$",price)  
if time<17:
    price=price-2.00 
    print("U are awarded a discount of $2.00")
    print("The final price of ticket is:$",price) 
