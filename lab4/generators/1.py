#Create a generator that generates the 
# squares of numbers up to some number N.

def sqr(n):
    for i in range(n):
        a=i**2
        yield a
        
n=int(input())
a=sqr(n)
b=list(a)
print(b)