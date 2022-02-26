from base64 import b64encode, b32encode, b64decode

with open("flag.txt") as f:
    flag = f.readline()

flag = flag.encode()

for i in range(9):
    flag = b64encode(flag)
for i in range(6):
    flag = b32encode(flag)   

with open("encoded", "w") as f1:
    f1.write(flag.decode())
