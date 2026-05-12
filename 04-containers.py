#containers in py like sets ,dict,tuple,list

#####################################list [" "," "," "]######################################
#muttable
list=["x",3,"@"]
print(len(list))

list1 = [1,2,3]
list2 = [4,5,6]
print(list1 + list2)
print(list1*2)

print(list1[0])
print(list1[2:6])
print(list1[2:])
print(list1[:5])
print(list1[-1])

del list1[0]
print(list1)

list1.append(11)
print(list1)
list1.pop()
print(list1)
list1.reverse()
print(list1)

l1=[10,30,20,60,40,50,]
l2 = [1,2,3,4]
l3=l1+l2
print(l3)
l3=l1*2
print(l3)

# list comprehension
even_squares=[x**2 for x in range(10) if x%2==0]
print(even_squares)

list = [1,5,3,77,4,2]
big=list[0]
for i in list:
    if i<big:
        big=i
print("smallest :",big)

list = [1,2,3,4,5,6]
for i in list:
print(i)
total =sum(list)

sum=0
for i in list:
    sum = sum+i
print(sum)

list= [5,3,4,77,1,2]
# result =list.index(77)
# print(result)

# print(list.index(77))
for i in list:
    result =list.index(77)
print(result)    
length = len(list)


list =[1,5,9,77,8]
middle = list[len(list)//2]
print(middle)

list=[1,2,3,4,5]
even=[]
odd=[]
for i in list:
    if i%2 == 0:
        even.append(i)  
    else:
        odd.append(i)
print("even:",even)
print("odd:",odd)    


#methods in list are:
# append method in list -- adding an element to end of a list
# clear method is used to clear all the elements form the list
# copy method used to copy all elements from one list to another
# count gives no of times a element has repeated in the list
# extend  list1+list2
# index to find the position
# insert method
# pop removes last element 
# remove is used to remove a particular element from the list
# reverse is used to reverse the elements in list
# '+' used for concatenation of two lists
# '*' used for repeating a list no.of times
# in python both arrays are solved using the list



#####################################tuples######################################
tuples-immutable (, , ,)

tuple1=("a","b","c")
tuple1=('a','b', 'c')
print(tuple1)

tuple1 = (1,2,3,4,5)
print(tuple1)
tuple2 = ("India","USA","Mexico","canada")
print(tuple2)

address = ("john",18,"yellow sterrt","mexico")
print(address)

country = ("usa","uk","canada","Germany","india")
if "germany" in country or "Germany" in country:
    print("Germany is present")
else:
    print("Germany is not present")

tuple[start:end:jumpindex]
t1=("pen","pencil","eraser","slate","marker")
print(t1[1:4])

values=(1,2,3,4,5,6,7,8,9)
print(values[4:8:2])
print(values[4:8: ])

country = ("usa","uk","canada","Germany","india")
# print(type(country))
temp = list(country)
# temp=country
# print(type(country))
print(temp)
temp.append("indian")
print(temp)
country1= tuple(temp)
print(country1)
print(type(country1))

#unpacking of tuples
info=("John",21,"Standford")
(name,age,university)=info
print("Name:",name)
print("Age:",age)
print("University:",university)

#####################################sets in python######################################
# set is a container { , , } duplicates are removed , immutable 

set={1,2,3}
print(set)
print(type(set))

tuple=(4,5,6)
print(tuple)
print(type(tuple))

list=[7,8,9]
print(list)
print(type(list))

set={1,2,3,3,2,1,5,6,4}
print(set)

#####################################dictionaries######################################
# dict = {key1:value1,key2:value2,key3:value3, ............}

dict1={"x":1,"y":2,"z":3}
print(dict1)

print(dict1["y"])

#changing/updating the values
dict1={"x":1,"y":2,"z":3}
dict1["y"] = 12
print(dict1)

couse ={"course":"pyhton",
        "version":3,
        "duration":"45days"}
print(couse)
# here the spelling of python is wrong so lets update it
couse["course"] = "python"
print("updated info:",couse)

courses = dict({1:"java",
           2:"python",
           3:"pandas"})
print(courses.get(2))

# for key,value in courses.items():
#     print(key,value)

for key in courses:
    print(key,courses[key])


