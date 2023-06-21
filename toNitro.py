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
        new.write((0x5247434E).to_bytes(4, "big"))
        new.write((0xFFFE0101).to_bytes(4, "big"))
        new.write((16 + 32 + size).to_bytes(4, "little"))
        new.write((0x10000100).to_bytes(4, "big"))
        new.write((0x52414843).to_bytes(4, "big"))
        new.write((32 + size).to_bytes(4, "little"))
        new.write((size // 2048).to_bytes(2, "little"))
        new.write((0x200003000000).to_bytes(6, "big"))
        new.write(bytes(8))
        new.write(size.to_bytes(4, "little"))
        new.write((0x18).to_bytes(4, "little"))
        new.write(file[16:])
        new.close()
    elif (val.endswith(".vce") == True):
        f = open(val, "rb")
        file = f.read()
        f.close()
        new = open("test.ncer", "wb")
        new.close()
        new = open("test.ncer", "ab")        
        
        offset = int.from_bytes(file[32:36], "little")
        size = int((len(file) - offset) * 14/8)
        new.write((0x5245434E).to_bytes(4, "big"))
        new.write((0xFFFE0001).to_bytes(4, "big"))
        new.write((16 + 32 + size).to_bytes(4, "little"))
        new.write((0x10000100).to_bytes(4, "big"))
        new.write((0x4B424543).to_bytes(4, "big"))
        new.write((32 + size).to_bytes(4, "little"))
        new.write(file[0x1C:0x1E])
        new.write(bytes(2))
        new.write((0x18).to_bytes(4, "little"))
        new.write((4).to_bytes(4, "little"))
        new.write(bytes(12))
        for i in range(size // 14):
            new.write((1).to_bytes(4, "little"))
            new.write((i * 6).to_bytes(4, "little"))
        for i in range(offset, len(file), 8):
            new.write(file[i:(i + 6)])
        new.close()
    