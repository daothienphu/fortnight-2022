from base64 import b64decode, b32decode

encoded_file = "encoded"   
with open(encoded_file, "r") as f:
    encoded = f.readline()

encoded = encoded.encode()
for i in range(6):
    encoded = b32decode(encoded)
for i in range(9):
    encoded = b64decode(encoded)

with open("flag.txt", "w") as f1:
    f1.write(encoded.decode())