# 1.A recipe you are reading states how many 
# grams you need for the ingredient. Unfortunately, 
# your store only sells items in ounces. 
# Create a function to convert grams to ounces. 
# ounces = 28.3495231 * grams
def firstfunc(x):
    return 28.3495231*x
grams=10
ounces=firstfunc(grams)
print(ounces)

# 2.Read in a Fahrenheit temperature. 
# Calculate and display the equivalent centigrade 
# temperature. The following formula is used for 
# the conversion: C = (5 / 9) * (F – 32)
def seconfunc(f):
    return (5 / 9) * (f - 32)
f=86
c=seconfunc(f)
print(c)
# 3.Write a program to solve a classic puzzle: 
# We count 35 heads and 94 legs among the chickens 
# and rabbits in a farm. How many rabbits and 
# how many chickens do we have? create function: 
# solve(numheads, numlegs):
def solve(numheads,numlegs):
    nosol='No solutions!'
    for i in range(numheads + 1):
        j=numheads-i
        if 2*i + 4*j ==numlegs:
            return i,j
        return nosol,nosol
numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print (solutions)

# 4.You are given list of numbers separated by 
# spaces. Write a function filter_prime which 
# will take list of numbers as an agrument and 
# returns only prime numbers from the list.

# 5.Write a function that accepts string from user 
# and print all permutations of that string.

def permutation(a, l, r):
    if l==r:
        print (a)
    else:
        for i in range(l,r):
            a[l],a[i]=a[i],a[l]
            permutation(a,l+1,r)
            a[l],a[i]=a[i],a[l]
            
string="ABC"
n=len(string)
a=list(string)
permutation(a,0,n)

# 6.Write a function that accepts string from user, 
# return a sentence with the words reversed. 
# We are ready -> ready are We
def reverseword(s, start, end):
    while start<end:
        s[start],s[end]=s[end],s[start]
        start=start+1
        end-=1
    
s="We are ready"
s=list(s)
start=0
while True:
    try:
        end=s.index(' ', start)
        reverseword(s,start,end-1)
        start=end+1
    except ValueError:
        reverseword(s,start,len(s)-1)
        break
s.reverse()
s="".join(s)
print(s)
# 7.Given a list of ints, return True if the array 
# contains a 3 next to a 3 somewhere.

#     def has_33(nums):
#         pass

#     has_33([1, 3, 3]) → True
#     has_33([1, 3, 1, 3]) → False
#     has_33([3, 1, 3]) → False
def has_33(numbs):
    for i in range(0,len(numbs)-1):
        if numbs[i:i+2]==[3,3]:
            return True
    return False

# 8. Write a function that takes in a 
# list of integers and returns True if it 
# contains 007 in order
# def spy_game(nums):
#     pass

#     spy_game([1,2,4,0,0,7,5]) --> True
#     spy_game([1,0,2,4,0,5,7]) --> True
#     spy_game([1,7,2,0,4,5,0]) --> False
def spygame(nums):
    for i in range(0, len(nums)):
        if nums[i]==0:
            for x in range (i+1,len(nums)):
                if nums[x]==0:
                    for y in range(x+1,len(nums)):
                        if nums[y]==7:
                            return True
                else:
                    return False
                
print(spygame[(1,2,4,0,0,7,5)])
# 9. Write a function that computes the volume of a sphere given its radius.
def volume(r):
    vol=(4/3)*3,14159*r*r*r
    return vol
radius=float(12)
print(volume(radius))

# 10.Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
def uniq(num):
    unique=[]
    for i in num:
        if i not in unique:
            unique.append(i)
    return unique
print(list([1,2,2,1,3,4]))
# 11. Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False
w="word"
ww="alila"
print(palindrome(w))
print(palindrome(ww))
# 12. Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

# ****
# *********
# *******
# 13. Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
#     Hello! What is your name?
#     KBTU

#     Well, KBTU, I am thinking of a number between 1 and 20.
#     Take a guess.
#     12

#     Your guess is too low.
#     Take a guess.
#     16

#     Your guess is too low.
#     Take a guess.
#     19

# 14. Good job, KBTU! You guessed my number in 3 guesses!
# Create a python file and import some of the functions from the above 13 tasks and try to use them.
# f4
# a = [int(x) for x in input().split()]
# y=[]
# print(a)
# filter_prime(a, y)
# print(y)