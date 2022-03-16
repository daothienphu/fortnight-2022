from pwn import *
from binascii import hexlify, unhexlify
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
conn = remote("103.245.249.107", 20314)
e = 0x10001
n = 0

def num_to_hex_str(num):
    return binascii.hexlify(long_to_bytes(num)).decode()

def hex_str_to_num(string):
    return bytes_to_long(binascii.unhexlify(string.encode()))

def to_sign(conn, msg, hex=False):
    print(conn.recvuntil("Your choice: ".encode()).decode())
    print("1")
    conn.sendline("1\n".encode())
    print(conn.recvuntil("Command to sign: ".encode()).decode())
    if hex == False:
        msg = hexlify(msg.encode()).decode()
    print(msg)
    conn.sendline((msg + "\n").encode())
    print(conn.recvline().decode())
    signed_cmd = conn.recvline().decode()
    print(signed_cmd)
    return signed_cmd

def to_verify(conn, cmd, get_output=False):
    print(conn.recvuntil("Your choice: ".encode()).decode())
    print("2")
    conn.sendline("2\n".encode())
    print(conn.recvuntil("Command to verify: ".encode()).decode())
    print(cmd)
    conn.sendline((cmd + "\n").encode())
    print(conn.recvline().decode())
    if get_output == True:
        pubkey = conn.recvline().decode()
        print(pubkey)
        return pubkey

signed_cmd = to_sign(conn, "get pubkey")
pubkey = to_verify(conn, signed_cmd, True)

n = int(pubkey.split(", ")[1][:-2])

cmd = bytes_to_long("peek flag".encode())
blinded_cmd = cmd * pow(5, e, n)
blinded_cmd = num_to_hex_str(blinded_cmd)

blinded_signed_cmd = to_sign(conn, blinded_cmd, True).strip()

blinded_signed_cmd = hex_str_to_num(blinded_signed_cmd)
blinded_signed_cmd = blinded_signed_cmd * inverse(5, n) % n
blinded_signed_cmd = num_to_hex_str(blinded_signed_cmd)

to_verify(conn, blinded_signed_cmd, True)
conn.close()