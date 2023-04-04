# Write a Python program to delete file 
# by specified path. Before deleting check 
# for access and whether a given path exists or not.

import os 
path = r'C:\Users\Admin\Desktop\study\2022-2023\Spring 2022-2023\pp2\delete.txt' 
if os.path.exists(path): 
    os.remove(path)
    
# for i in range(65,91):
#     with open(chr(i)+'.txt', 'x') as f:
#         f.write("Hello world")