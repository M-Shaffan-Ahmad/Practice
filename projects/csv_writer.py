import csv



data=["shaffan", "ahmad", "zenron", "squid890$", "28/05/2004", "hannah@gmail.com", "44 1234567895"]
file = open("User_data", "w")
writer=csv.writer(file)
writer.writerow(data)

file.close()



file=open("User_data")
reader=csv.reader(file)
row=[]
rows=[]

try:
    for i in range(1000000):
        row=next(reader)
        rows.append(row)
except StopIteration:
    rows.pop()


for i in rows:
    print(i)



