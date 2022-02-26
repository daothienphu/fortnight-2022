from pwn import *
conn = remote("0.0.0.0", 69)

KEY_LENGTH = 6900

conn.recvuntil("Here is the ecrypted flag:".encode())
encrypted_flag = conn.recvline()
flag_length = len(encrypted_flag) // 2
tmp = "a"

while True:
    conn.recvuntil("Your message: ")
    
    msg_to_send = "a"*min(1000, KEY_LENGTH - flag_length)*2
    conn.send(msg_to_send.encode())
    
    conn.recvuntil("Encrypted message: ")
    conn.recvline()
    
    KEY_LENGTH -= len(msg_to_send)
    if KEY_LENGTH == 0:
        break

conn.recvuntil("Your message: ")
conn.send(encrypted_flag)
conn.recvuntil("Encrypted message: ")
flag = conn.recvline()
conn.close()

print("The flag is: " + bytearray.fromhex(flag).decode())