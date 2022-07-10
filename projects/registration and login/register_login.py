#PROGRAM FOR LOGIN AND REGISTRATION
from tkinter import *
from file_sorting import file_sort

y_axis = 60
height_entry = 10
seperator=15

#DEFS START

def file_set():
	file_sort("Users_credentials.txt")
	root.destroy()

def clean():
	result("      "*20,)
	i=0
	while True:
		result("       "*15,240, y_axis+i)
		i+=20
		if i ==160:
			break

def result(display, a=100, n=230+seperator):
	result = Label(root, text=display, font=("Calibri", "10"))
	result.place(x=a, y=n+seperator)

def clear_fields(): #working perfect
	first.delete(0,END)
	last.delete(0, END)
	username.delete(0, END)
	password.delete(0, END)
	dob.delete(0, END)
	email.delete(0, END)
	phone_no.delete(0, END)
	clean()

def collect_log(): #fine
	clean()
	info =[username.get(),password.get(),dob.get()]

	output_text = "Invalid credentials, please register if not registered yet"

	file = open("Users_credentials.txt", "r")
	for data in file:
		#data = file.readline()
		data = data.split()

		name = []
		for i in data:
			i = i.strip("[]")
			i = i.strip(",")
			i = i.strip("\'")
			name.append(i)
		if name[2] == info[0] and name[3] == info[1] and name[4] == info[2]:
			output_text = "Successful logged in"

	result(output_text)

def collect_reg(): #working fine
	clean()

	#Validation of entry
	first_check= first.get()
	first_check_pass=False
	check= first_check.isalpha()
	if first_check=="":
		result("Please fill the field", 240, y_axis)
	elif check == False:
		result("Please enter a name in alphabets", 240, y_axis)
	else:
		first_check_pass=True

	last_check = last.get()
	last_check_pass=False
	check = last_check.isalpha()
	if last_check == "":
		result("Please fill the field", 240, y_axis+20)
	elif check == False:
		result("Please enter a name in alphabets", 240, y_axis+20)
	else:
		last_check_pass = True

	username_check = username.get()
	username_check_pass=False
	if username_check == "":
		result("Please fill the field", 240, y_axis+40)
	elif check == False:
		result("Please enter a name in alphabets", 240, y_axis+40)
	else:
		username_check_pass = True

	password_check = password.get()
	password_check_pass=False
	if password_check == "":
		result("Please fill the field", 240, y_axis + 60)
	else:
		password_check_pass = True

	dob_check = dob.get()
	dob_check_pass=False
	month = dob_check[3:5]
	try:
		check = dob_check[2], dob_check[5]
	except IndexError:
		check=[1,2]
	try:
		if 0 < int(month) < 13:
			month_check = True
		else:
			month_check = False
	except ValueError:
		month_check = False

	if dob_check == "":
		result("Please fill the field", 240, y_axis + 80)
	elif check != ('/', '/') or len(dob_check) != 10 or month_check==False:
		result("Invalid Date of birth", 240, y_axis + 80)
	else:
		dob_check_pass=True

	email_check = email.get()
	email_check_pass=False
	check =email_check.find("@")
	check2 = email_check[-4:]
	if email_check == "":
		result("Please fill the field", 240, y_axis + 100)
	elif check == -1 or check2 != ".com":
		result("PLease enter a valid email address", 240, y_axis + 100)
	else:
		email_check_pass=True

	phone_no_check = phone_no.get()
	phone_no_check_pass=False
	a="".join(phone_no_check.split())
	check=a.isnumeric()
	if phone_no_check=="":
		result("Please fill the field", 240, y_axis + 120)
	elif check==False or len(phone_no_check)!=13:
		result("Please enter a valid phone number,\ne.g(44 1245548979)", 240, y_axis + 120)
	else:
		phone_no_check_pass=True

	if first_check_pass and last_check_pass and username_check_pass and password_check_pass and dob_check_pass and email_check_pass and phone_no_check_pass:
		data = [first.get(), last.get(), username.get(), password.get(), dob.get(), email.get(), ("+"+phone_no.get())]
		user_file = open("Users_credentials.txt", "a")
		user_file.write(str(data) + "\n")
		user_file.close()

		result("You are successfully registered")

def regg(): #wroking perfect
	clear_fields()
	#display
	first_.place(x=40, y=y_axis+seperator)
	first.place(x=110, y=y_axis+seperator)

	last_.place(x=40, y=y_axis + 20+seperator)
	last.place(x=110, y=y_axis + 20+seperator)

	email_.place(x=40, y=y_axis + 100+seperator)
	email.place(x=110, y=y_axis + 100+seperator)

	phone_no_.place(x=40, y=y_axis + 120+seperator)
	phone_no.place(x=110, y=y_axis + 120+seperator)

	login_button.place_forget()
	register_button.place(x=110, y=y_axis + 140+seperator)

	clean()

def logg(): #working perfect
	clear_fields()
	login_button.place(x=190, y=y_axis + 140+seperator)

	register_button.place_forget()
	first.place_forget()
	last.place_forget()
	email.place_forget()
	phone_no.place_forget()
	first_.place_forget()
	last_.place_forget()
	email_.place_forget()
	phone_no_.place_forget()
	clean()

#DEFS ENDS




#DISPLAY
root = Tk()
root.title("Registration and Login")
root.geometry("450x350")

#Main display
heading = Label(root, text="Registration and Login", font=("Calibri", "20"))
heading.place(x=40, y=8)

username = Entry(root, font=("Calibri", height_entry))
username_ = Label(root, text="Username")

password = Entry(root,font=("Calibri", height_entry))
password_ = Label(root, text="Password")

dob = Entry(root, width=14,font=("Calibri", height_entry))
dob_ = Label(root, text="Dob (DD/MM/YYYY)")

username_.place(x=40, y=y_axis+ 40+seperator)
username.place(x=110, y=y_axis+ 40+seperator)

password_.place(x=40, y=y_axis + 60+seperator)
password.place(x=110, y=y_axis + 60+seperator)

dob_.place(x=40, y=y_axis + 80+seperator)
dob.place(x=153, y=y_axis + 80+seperator)


login_button = Button(root, text="Login", command=collect_log)
login_button.place(x=190, y=y_axis + 140+seperator)


registering = Button(root, text="Register", bd=3, command=regg)
registering.place(x=130, y=y_axis + 220+seperator)

or_block = Label(root, text="or", font=("Calibri", "15"))
or_block.place(x=190, y=y_axis + 220+seperator)
login = Button(root, text="Login", bd=3, command=logg)
login.place(x=220, y=y_axis + 220+seperator)

#registration display start
first = Entry(root,font=("Calibri", height_entry))
first_ = Label(root, text="First name")
last = Entry(root,font=("Calibri", height_entry))
last_ = Label(root, text="Last name")

email = Entry(root,font=("Calibri", height_entry))
email_ = Label(root, text="Email")

phone_no = Entry(root,font=("Calibri", height_entry))
phone_no_ = Label(root, text="Phone no.")

register_button = Button(root, text="Register", command=collect_reg)
#registration display end

logg()
root.protocol("WM_DELETE_WINDOW", file_set)
root.mainloop()



