# Write a Python program to list only directories, 
# files and all directories, files in a specified 
# path.

from genericpath import isdir 
import os
 
path = r'C:\Users\Admin\Desktop\study\2022-2023\Spring 2022-2023\pp2\lab6\dirfiles' 
print('DIRECT:') 
for j in os.listdir(path): 
    # z = os.path.join(path,j)#соединяем пути  
    # print(z) 
    if os.path.isdir(os.path.join(path, j)): 
        print(j) 
print('FILES:') 
for j in os.listdir(path): 
    if os.path.isdir(os.path.join(path, j))!=True: 
        print(j) 
print('FILES and DIREC:') 
for j in os.listdir(path): 
    print(j)