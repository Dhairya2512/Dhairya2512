print("Hello world")

#using of variable

a,b,c = 10,20.5,"Dhairya Popat"

print(a)
print("value of b :",b)
print("user name:",c)

# changing the values of a variable
name = "Akash technolabs"
print("Name is :",name)
#assigning new values
name = "Akashsir.com"
print("Name is :",name)

#int datatype
n1 = 10
print(n1 ,"is of type",type(n1))
n2 = 10.5
print(n2 ,"is of type",type(n2))
print(n2 ,"is a complex number?",isinstance(10.5,int))
n3 = 1+3j
print(n3,"is a complex number?",isinstance(1+3j,complex))

#string Datatype

name = "Dhairya"
print(name)
print(name[2])
print(name[1:5])
print(name[3:])
print(name[:5])
print(name*2)
print("My name is" + name)

# List Datatype
l1=[10,20,30.5,"Dhairya"]
print(l1)
print(type(l1))
print(l1[1])
print(l1[1:3])
print(l1[2:])
print(l1[:3])

# Tuple Datatype
t1=(10,20,30.5,"Dhairya")
print(t1)
print(type(t1))
print(t1[2])
print(t1[2:3])
print(t1[2:])
print(t1[:1])

#dictionary Datatype
d1= {1: "dhairya",2:"hello","a1":100}
print(d1)
print(type(d1))
print(d1[1])
print(d1[2])
print(d1["a1"])
