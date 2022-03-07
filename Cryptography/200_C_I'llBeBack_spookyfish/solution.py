from pwn import *
conn = remote("103.245.249.107", 20302)

KEY_LENGTH = 6900

print(conn.recvuntil("Here is the ecrypted flag:".encode()).decode())
encrypted_flag = conn.recvline().decode().strip()
print(encrypted_flag)
flag_length = len(encrypted_flag) // 2

KEY_LENGTH -= flag_length

while True:
    print(conn.recvuntil("Your message: ".encode()).decode())
    
    msg_to_send = "a"*min(1000, KEY_LENGTH)*2
    print(msg_to_send)
    conn.send(msg_to_send.encode())
    
    print(conn.recvuntil("Encrypted message: ".encode()).decode())
    print(conn.recvline())
    
    KEY_LENGTH -= len(msg_to_send) // 2
    print("Key length left: ",KEY_LENGTH)
    if KEY_LENGTH == 0:
        break

print(conn.recvuntil("Your message: ".encode()).decode())
print(encrypted_flag)
conn.send((encrypted_flag + "\n").encode())
print(conn.recvuntil("Encrypted message: ".encode()).decode())
flag = conn.recvline().decode().strip()
print(flag)
conn.close()

print("The flag is: " + bytearray.fromhex(flag).decode())