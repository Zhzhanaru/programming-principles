# Write a Python program with builtin function that accepts a string 
# and calculate the number of upper case letters and lower case letters 

words=str(input().split())
cnt1=0
cnt2=0

for i in words:
    if i.islower():
        cnt1+=1
    if i.isupper():
        cnt2+=1
print(f'Number of lowercase characters is:{cnt1}')       
print(f'Number of uppercase characters is:{cnt2}')
