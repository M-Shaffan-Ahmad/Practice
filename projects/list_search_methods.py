
def linear_search(a, list):
    o = 1
    for n in list:
        if a == n:
            return o
        else:
            n += 1
            o +=1

list = [1,2,5,4,8,44,55,66,11,22,33,88]
print(binary_search(11,list))



