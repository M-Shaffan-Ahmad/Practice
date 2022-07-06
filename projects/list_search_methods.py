def binary_search(a, num_list):
    original_list= num_list.copy()
    num_list.sort()

    while True:
        n = len(num_list) // 2
        if a == num_list[n]:
            o = original_list.index(num_list[n])
            return f"the number is at position {o+1}"
        elif a < num_list[n]:
            num_list = num_list[:n]
        else:
            num_list = num_list[n:]



def linear_search(a, list):
    for n in list:
        if a == n:
            return list.index(n) + 1



