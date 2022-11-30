
'# 1....

# def ask_question():
#     print("once")
# ask_question()
# ask_question()
# ask_question()
# ask_question()
# ask_question()
 
# 2....

# def ask_question():
#     print("hello")
# ask_question()
# ask_question()
# ask_question()

# 3....

# number=[3,5,7,34,2,89,2,5]
# print(max(number))

# 4....

# number=[1,2,3,4,5]
# print(sum(number))

# 5...

# a=[6,8,4,3,9,56,0,34,7,15]
# print(sorted(a))

# 6....

# a=["Z","A","A","B","E","M","A","R","D"]
# a.reverse()
# print(a)

# 7.....

# a=[8,6,4,8,4,50,2,7]
# print(min(a))

# 8....

# def sum():
#     print(12+13)
# sum()

# def sum(a,b):
#     c=a+b
#     print(c)
# sum(12,13)

# # 9....

# def welcome():
#     print("welcome to function")
# welcome()

# def even():
#     if 13%2==0:
#         print("even number")
#     else:
#         print("odd number")
# even()


# function argument 

# 1...

# def my_function(name):
#     print(name)
# my_function("emil")
# my_function("tobias")
# my_function("linus")

# 2...

# a=[1,2,3,7,7,4,8]
# print(max(a))

# 3....

# a=[1,2,3,4,5,6]
# print(len(a))

# 4....

# def a(name):
#     print("hello",name)
#     print("how are you")
# a("aatif")


# 5....

# def add_numbers(number1,number2):
#     print("i will add two numbers")
#     print(number1+number2)
# add_numbers(120,50)
# num_x="134"
# name="rinki"
# add_numbers(num_x,name)


# 6....

# def say_hello_language(name,language):
#     if language=="hindi":
#         print("namaste",name)
#         print("aap kese ho")
#     elif language=="pangabi":
#         print("sat sri akal",name)
#         print("tuhada ki haal hai")
#     else:
#         print("Hello",name)
#         print("How are you")
#     say_hello_language("Rishabh","Punjabi")
#     say_hello_language("Armaan","english")
#     say_hello_language("Abhishek","french")
#     say_hello_language("kavay","hindi")

# 7....

# def say_hello_people(name_x,name_y,name_z,name_a):
#     print("Namaste",name_x)
#     print("Alah hafiz",name_y)
#     print("Bonjour",name_z)
#     print("Hello",name_a)
# say_hello_people("Imitiyaz","Rishabh","Rahul","Vidiya")
# say_hello_people("Steve","Saswata","Shakrudin","Rajeev")


# 8....

# def a(flavours):
#     print("I love"+flavours)
# a("choclate")
# a("Strabarry")
# a("Pizza")
# a("Sandwich")


# 9....

# def attendence(name,status="absent"):
#     print(name,"is",status,"today")
# attendence("kartik","present")
# attendence("Sonu")
# attendence("vishal","present")
# attendence("umesh")

# ex..1...

# def a(name):
#     print("Welcome",name)
# a("Rinki")
# a("Vishal")
# a("Kartik")
# a("Bijender")


# # ex..2..

# def a(name,age):
#     print(name,"is",age,"year old")
# a("tannu","19")
# a("shivani","17")
# a("swati","19")

# ex..3...

# def a(name,topic,mentor):
#     print("Hello",name,"your",topic,"concept","is clear the help of",mentor)
# a("tannu","loop","swati")


# ex..4...

# def a(name,founder):
#     print("My name is",name)
#     print("I am the cofounder of",founder)
# a("swati","navgurukul")


# ex..5...

# def add(a,b):
#     print(a+b)
# add(12,56)

# ex..6...

# def x(a,b):
#     if(a%2==0 and b%2==0):
#         print("both are even")
#         print(a/2,b/2)
#     else:
#         print("both number are not even")
# x(10,20)


# ex..7...

# def x(a,b):
#     for i in range(len(a)):
#         if(a[i]%2==0 and b[i]%2==0):
#             print("both are even")
#         else:
#             print("both number are not even")
# i1=[10,13,20,21,22]
# i2=[16,18,19,21,27]
# x(i1,i2)


# ex..8...

# def a(x,y):
#     num_sum=x+y
#     return num_sum
# sum1=a(20,40)
# print(sum1)
# sum2=a(560,23)
# c=1234
# d=12
# sum3=a(c,d)
# print(sum2)
# print(sum3)
# num=a(20,40)/a(5,1)
# print(num)


# ex..9...

# def a(x,y):
#     print(x+y)
# sum=a(4,5)
# print(sum)
# print(type(sum))

# def a(x,y):
#     print(x+y)
# a(4,5)

# ex..10...

# def a(x,y):
#     print(x*y)
# a(5,12)

# ex..11...

# def a(x,y):
#     print(x+y)
#     print("Hello from navgurukul")
#     print("Will i reach")
# a(100,200)

# ex..12...

# def menu(day):
#     if day=="Monday":
#         return "Butter chicken"
#     elif day=="Tuesday":
#         return "Pizza"
#     else:
#         return "Chole bhature"
#     print("Will i able to print")
# mon_menu=menu("Monday")
# print(mon_menu)
# tues_menu=menu("tuesday")
# print(tues_menu)
# fri_menu=menu("friday")
# print(fri_menu)


# ex..13...

# def menu(day):
#     if day=="Monday":
#         food="Butter chicken"
#     elif day=="Tuesday":
#         food="Pizza"
#     else:
#         food= "Chole bhature"
#     print("Will i able to print")
#     return food
#     print("But i am not sure will print")
# print(menu("monday"))

# ex..6(part-1):

# def calculate(x,y,operation):
#     if (operation=="add"):
#         print(x+y)
#     elif(operation=="sub"):
#         print(x-y)
#     elif(operation=="mul"):
#         print(x*y)
#     elif(operation=="divide"):
#         print(x/y)
#     else:
#         print("invalid request")
# calculate(5,4,"add")


# ex..6(part-2):


# def calculate(x,y,operation):
#     i=[]
#     if (operation=="add"):
#              print(x+y)
#     elif(operation=="sub"):
#     elif(operation=="multiply"):
#         for i in range(len(x)): 
#             mul=x[i]*y[i]
#             i.append(mul)
#         print(i)
#     else:
#         print("invalid request")
# i1=[10,20,30,40]
# i2=[50,60,70,80]
# calculate(i1,i2,"multiply")

# ex...@1..

# def f1():
#     s="I love navgurukul"
#     def f2():
#         print(s)
#     f2()
# f1()


# ex...@2..

# def f1():
#     s="I love india"
#     def f2():
#         print(s)
#     f2()
# f1()

# ex...@3..

# def f1():
#     a="I love india"
#     def f2():
#         b="My name is tannu"
#         print(b)
#     f2()
#     print()
# f1()

# ex...@4..

# def distance(kms):
#     if kms<20:
#         print("Close")
#     elif kms<50:
#         print("Median")
#     else:
#         print("far")
# distance(20)


# ex...@5..

# x=50
# def func(x):
#     print('x is',x)
#     x=2
#     print('changed local x to',x)
# func(x)
# print('x is now',x)