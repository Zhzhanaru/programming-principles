# Write a Python program to find 
# sequences of lowercase 
# letters joined with a underscore.

import re

s=input()
x=re.findall('[a-z]+_[a-z]+',s)
print(x)

if x:
    print("There is a match")
else:
    print("None")