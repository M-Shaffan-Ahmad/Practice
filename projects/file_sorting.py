def file_sort(file):
    try:
        old = open(file, "r")
        datat = old.readline()
        set = {datat}
        data = old.readlines()
        for row in data:
            set.add(row)
        old.close()
        new = open(file, "w")
        for i in set:
            new.writelines(i)
        new.close()
    except FileNotFoundError:
        a=0



