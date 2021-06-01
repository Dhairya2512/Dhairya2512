# Functions in Python

def my_function():
    print("Hello world")

my_function()

#Example with Argument

def my_function(name):
    print("Name is :",name)

my_function("Dhairya")

# Example of Return Statement

def my_function(name):
    return name
name = my_function("Dhairya")
print(name)

# Example of Multiple return statement

def my_function():
     name= "Dhairya"
     contact = 9876543210
     return name ,contact
name ,contact =my_function()
print("Name is :", name)
print("contact :" ,contact)

# Python Default Arguments

def sum (a=5,b=7):
    print(a+b)

sum(10,20)
sum()

#python Keyword Arguments

def sum(a,b):
    print("sum is:",a+b)

sum(b=10,a=5)

#Variable-length (non keyword Argument)

def add(*num):
    sum = 0

    for n in num:
        sum = sum + n
        print("sum :",sum)

add(10,30)
add(10,30,40)

#scope of variable

def my_func():
    x= 10
    print("value inside function :",x)

x =20
my_func()
print("value outside function :",x)

#Arithmetic Operater

x=10
y = 5
print("x+y=",x+y)
print("x-y=",x-y)
print("x*y=",x*y)
print("x/y=",x/y)
print("x//y=",x//y)
print("x**y=",x**y)

#Comparison Operater

x= 10
y =6
print("x>y is",x>y)
print("x<yis",x<y)
print("x==y is",x==y)
print("x!=y is",x!=y)
print("x>=y is",x>=y)
print("x<=y is",x<=y)

#Identity Operator

x=20
y =20
print(x is y)
print(x is not y)

#Membership operator

x=10
y=6
list1 = [10,20,30,40]
print(x in list1)
print(y in list1)
print(y not in list1)

# Logical Operater
#And operater
x = 5

print(x > 3 and x < 10)

# Or operater
x = 5

print(x > 3 or x < 4)

# Not operater

x = 5

print(not(x > 3 and x < 10))
