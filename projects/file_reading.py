def file_read(file):
	text = open(file, "r")
	list=[]
	for data in text:
		data = data.split()
		name = []
		for i in data:
			i = i.strip("[]")
			i = i.strip(",")
			i = i.strip("\'")
			name.append(i)
		list.append(name)
	return list

print(file_read("registration and login/Users_credentials.txt"))

