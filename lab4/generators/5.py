# Implement a generator that returns 
# all numbers from (n) down to 0.
def num(n):
    for i in range(n,-1,-1):
        yield i
        
n=int(input())
a=num(n)
ans=list(a)

print(ans)