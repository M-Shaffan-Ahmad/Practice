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


#bin 2 hex



