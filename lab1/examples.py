#intro
print("Hello,World!")

#syntax
if 5>2:
    print("five is greater than two")
    
#creating comment
print("Zhanaru")
#comment

#variables
x=5
y="Zhanaru"
print(x)
print(y)
print(x,y)

z=20
z="Zhanaru"
print(z)

#variables:casting
a=str(3)
b=int(5)
c=float(3)
print(a,b,c)

#variables:get the type
q=5
r="Zhanaru"
print(type(q),type(r))

#single-double quotes
n='John'
y="Zhanaru"
print(n,y)

#case sensitive
e=2
E="ZHanaru"
print(e,E)

#list
fruits=["apple","banaana","orange"]
m,b,v=fruits
print(m,b,v)

#output variables
t="This "
h="is "
i="an "
s="apple"
print(t+h+i+s)

#global
l = "awesome"

def func():
  print("Python is " + l)

func()

#DATATYPES
x="hello"#str
x=20#int
x=20.5#float
x=1j#complex
x=["apple","juice"]#list
x=("apple","juice")#tuple
x=range(6)#range
x={"name":"John","age":"20"}#dict
x={"apple","bananas"}#set
x=frozenset({"apple","bananas"})#frozenset
x=True#bool
x=b"hello"#bytes
x=bytearray(5)#bytearray
x=memoryview(bytes(5))#memoryview
x=None#Nonetypes


#Casting
x=int(1)#->1
y=int(3.2)#->3
z=("3")#->3

x = float(1)     
y = float(2.8)   
z = float("3")   
w = float("4.2")

#strings
print("jello")

#print('hee')
a="hello"
print(a[1])#->it shows "e"

b = "Hello, World!"
print(b[2:5])

a = "Hello, World!"
print(a.upper())
print(a.lower())
a = " Hello, World! "
print(a.strip())

a = "Hello"
b = "World"
c = a + " " + b
print(c)

a = "Hello"
b = "World"
c = a + b
print(c)

#if else
a = 33
b = 200
if b > a:
  print("b is greater than a")
  
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
if a > b: print("a is greater than b")