# DENARY TO BINARY
def dec2bin(num):
    binary=""
    while num>0:
        binary += str(num%2)
        num //= 2
    binary = binary[::-1]
    return binary

#BINARY TO DENARY
def bin2dec(num):
    pov = 0
    denary = 0
    place = -1
    binary = str(num)
    for i in range(len(num)):
        denary+= int(num[place]) * (2**pov)
        place -= 1
        pov +=1
    return denary

#DEC 2 hex
def dec2hex(num):
    hex = ""
    while num>0:
        hexa = num%16
        if hexa == 10:
            hex += "A"
        elif hexa == 11:
            hex += "B"
        elif hexa == 12:
            hex += "C"
        elif hexa == 13:
            hex += "D"
        elif hexa == 14:
            hex += "E"
        elif hexa == 15:
            hex += "F"
        else:
            hex += str(hexa)
        num //= 16
    hex = hex[::-1]
    return num


#BIN 2 HEX
def bin2hex(num):
    num = bin2dec(num)
    num = dec2hex(num)
    return num


# HEX TO DEC
def hex2dec(num):
    pov = 0
    pos = -1
    denary = 0
    for i in range(len(str(num))):
        if num[pos] == "F":
            hex = 15
        elif num[pos] =="E":
            hex = 14
        elif num[pos] == "D":
            hex = 13
        elif num[pos] == "C":
            hex = 12
        elif num[pos]=="B":
            hex = 11
        elif num[pos]=="A":
            hex =10
        else:
            hex = int(num[pos])
        denary += hex * (16**pov)
        pos -= 1
        pov +=1
    return denary

print(hex2dec("1000"))

#HEX 2 BIN
def hex2bin(num):
    str(num)
    num = hex2dec(num)
    num = dec2bin(num)
    return num

print(hex2bin(1000))

