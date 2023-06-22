import os
import sys

for val in sys.argv[1:]:
    if (val.endswith(".vcl") == True):
        f = open(val, "rb")
        file = f.read()
        f.close()
        new = open("test.nclr", "wb")
        new.close()
        new = open("test.nclr", "ab")

        size = len(file) - 8
        new.write((0x524C434E).to_bytes(4, "big"))
        new.write((0xFFFE0001).to_bytes(4, "big"))
        new.write((16 + 24 + size).to_bytes(4, "little"))
        new.write((0x10000100).to_bytes(4, "big"))
        new.write((0x54544C50).to_bytes(4, "big"))
        new.write((24 + size).to_bytes(4, "little"))
        new.write((3).to_bytes(4, "little"))
        new.write(bytes(4))
        new.write(size.to_bytes(4, "little"))
        new.write((16).to_bytes(4, "little"))
        new.write(file[8:])
        new.close()
    elif (val.endswith(".vcg") == True):
        f = open(val, "rb")
        file = f.read()
        f.close()
        new = open("test.ncgr", "wb")
        new.close()
        new = open("test.ncgr", "ab")

        size = len(file) - 16
        mod = ((size // 32) % 32) * 32
        new.write((0x5247434E).to_bytes(4, "big"))
        new.write((0xFFFE0101).to_bytes(4, "big"))
        new.write((16 + 32 + size + mod).to_bytes(4, "little"))
        new.write((0x10000100).to_bytes(4, "big"))
        new.write((0x52414843).to_bytes(4, "big"))
        new.write((32 + size + mod).to_bytes(4, "little"))
        new.write(((size + mod) // 2048).to_bytes(2, "little"))
        if (file[4] == 0):
            new.write((0x200003000000).to_bytes(6, "big"))
        else:
            new.write((0x200004000000).to_bytes(6, "big"))
        new.write(bytes(8))
        new.write((size + mod).to_bytes(4, "little"))
        new.write((0x18).to_bytes(4, "little"))
        new.write(file[16:])
        new.write(bytes(mod))
        new.close()
    elif (val.endswith(".vce") == True):
        f = open(val, "rb")
        file = f.read()
        f.close()
        new = open("test.ncer", "wb")
        new.close()
        new = open("test.ncer", "ab")        
        
        offset = int.from_bytes(file[32:36], "little")
        spOffset = int.from_bytes(file[24:28], "little")
        spNum = int.from_bytes(file[20:24], "little")
        size = (spNum * 8) + int((len(file) - offset) * 0.75)
        new.write((0x5245434E).to_bytes(4, "big"))
        new.write((0xFFFE0001).to_bytes(4, "big"))
        new.write((16 + 32 + size).to_bytes(4, "little"))
        new.write((0x10000100).to_bytes(4, "big"))
        new.write((0x4B424543).to_bytes(4, "big"))
        new.write((32 + size).to_bytes(4, "little"))
        new.write(file[20:22])
        new.write(bytes(2))
        new.write((0x18).to_bytes(4, "little"))
        new.write((4).to_bytes(4, "little"))
        new.write(bytes(12))
        for i in range(spOffset, offset, 4):
            new.write(int.from_bytes(file[(i + 2):(i + 4)], "little").to_bytes(4, "little"))
            new.write((int.from_bytes(file[i:(i + 2)], "little") * 6).to_bytes(4, "little"))
        for i in range(offset, len(file), 8):
            # payload = int.from_bytes(file[i:(i + 6)], "little")
            # tile = (payload >> 32) & 0x3FF
            # print(tile)
            new.write(file[i:(i + 4)])
            big = int.from_bytes(file[(i + 4):(i + 6)], "little")
            ten = "0b" + bin(big)[2:][-10:]
            mult = int(ten, 2) * 4
            final = bin(big)[2:][0:-10] + ("0" * (10 - len(bin(mult)[2:]))) + bin(mult)[2:]
            new.write(int(final, 2).to_bytes(2, "little"))           
        new.close()
    elif (val.endswith(".vsc") == True):
        f = open(val, "rb")
        file = f.read()
        f.close()
        new = open("test.nscr", "wb")
        new.close()
        new = open("test.nscr", "ab")

        size = len(file) - 20
        new.write((0x5243534E).to_bytes(4, "big"))
        new.write((0xFFFE0001).to_bytes(4, "big"))
        new.write((16 + 20 + size).to_bytes(4, "little"))
        new.write((0x10000100).to_bytes(4, "big"))
        new.write((0x4E524353).to_bytes(4, "big"))
        new.write((20 + size).to_bytes(4, "little"))
        new.write((int.from_bytes(file[12:16], "little") * 8).to_bytes(2, "little"))
        new.write((int.from_bytes(file[16:20], "little") * 8).to_bytes(2, "little"))
        new.write(bytes(4))
        new.write((size).to_bytes(4, "little"))
        new.write(file[20:])
        new.close()
        