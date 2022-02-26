from base64 import b64encode, b32encode, b64decode
import re


flag = "f0rtn1ght{random_flag}".encode()
for i in range(6):
    flag = b64encode(flag)
print(flag.decode())
for i in range(9):
    flag = b32encode(flag)
print(flag.decode())    
