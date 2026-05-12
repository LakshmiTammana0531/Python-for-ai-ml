
#####functions########
## a function is a block of reusable code which can be called again when it is needed, it avoids repetition of code 

# def function_name(parameters):
    # code block
    # return value   (optional) 

# def sum(x, y):
#     return(x+y)
# print(sum(3,2))

# def mul(a,b):
#     print(a*b)
# mul(2,6)

# def sum(n,a):
#     print("name:",n,"\n","age:",a)
# sum("john",15)

# def sum(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def div(a,b):
#     print(a/b)
# sum(10,5)
# sub(10,5)
# mul(10,5)
# div(10,5)

# def table(a):
#     for i in range(1,11):
#         print(a,"*",i,"=",a*i)    
# table(5)

# def even(a):
#     for i in range(100, 1 , -2):
#         if i%2 == 0:
#             print(i)
# even(1)

# def function1():
#     n=5
#     def function2():
#         print(n)
#     function2()   
# function1() 

# def square(x):
#     return x**2
# print(square(3))

# def multiply(x,y):
#     return x*y
# print(multiply(3,2))

# def minmax(data):
#   return min(data), max(data)  
# print(minmax([1,3,7,2,10]))

# def findlargest(a,b,c):
#     if (a>b and a>c):
#       big=a
#     elif(b>a and b>c):
#        big=b
#     else:
#        big=c
#     return big
# x=int(input("Enter the first value:"))     
# y=int(input("Enter the second value:"))     
# z=int(input("Enter the third value:"))  

# res = findlargest(x,y,z)
# print("Maximum value is:",res)

# def fun(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fun(n-1)     
# fun(3)

# def fun(n):
#     if n==6:
#         print("Done")
#     else:
#         print(n)
#         fun(n+1)
# fun(1)          
    # for i in n:
        # result=i*n
        # print(result)
        # fun(n+1)



######################################file handling######################################

# file handling--create,read,write,delete 
## w-write
## r-read
## a-append
## x-create

# file = open("temp1.txt","w")
# file.write("My name is XXXXXXX ")
# file.close()
##### this creates a file with name temp1 and text as XXXXXXXXXXXXX 

# file = open("temp2.txt","w")
# file.write("I am studying in YYYYYYYY ")
# file.close()

# # file = open("temp3.txt","w")
# # file.write("pursuing B.TECH ")
# # file.close()

# file = open("temp4.txt","w")
# file.write("B.TECH in AIML ")
# file.close()

# file = open("temp5.txt","w")
# file.write("AIML in 4 th year 1st sem ")
# file.close()

# import os
# os.remove("temp5.txt")

# file = open("temp1.txt","r")
# print(file.read())
# file.close()

# file = open("temp1.txt","a")
# (file.write(",age is 20"))
# file.close()
