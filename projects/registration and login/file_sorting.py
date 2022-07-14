import csv
def file_sort(file):
    try:
        old = open(file, "r")
        datat = old.readline()
        set = {datat}
        data = old.readlines()
        for row in data:
            if row!=" " or row!=[]:
                set.add(row)
        try:
            set.remove('\n')
        except KeyError:
            a=1
        old.close()
        new = open(file, "w")
        for i in set:
            new.writelines(i)

        new.close()
    except FileNotFoundError:
        a=0

