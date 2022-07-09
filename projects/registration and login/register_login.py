#PROGRAM FOR LOGIN AND REGISTRATION
import fileinput
from tkinter import *




#defs
def clear_fields(): #working perfect
	first.delete(0,END)
	last.delete(0, END)
	username.delete(0, END)
	password.delete(0, END)
	dob.delete(0, END)
	email.delete(0, END)
	phone_no.delete(0, END)
	clean = Label(root, text="                                                                                                         ")
	clean.place(x=70, y =y_axis+170)


def collect_log(): #fine
	clean = Label(root, text="                                                                                                        ")
	clean.place(x=70, y =y_axis+170)
	info =[username.get(),password.get(),dob.get()]

	output_text = "Invalid credentials, please register if not registered yet"

	file = open("Users_credentials.txt", "r")
	for data in file:
		#data = file.readline()
		james = []
		data = data.split()

		name = []
		for i in data:
			i = i.strip("[]")
			i = i.strip(",")
			i = i.strip("\'")
			name.append(i)
		if name[2] == info[0] and name[3] == info[1] and name[4] == info[2]:
			output_text = "Successful logged in"

	result = Label(root, text=output_text, font=("Calibri", "10"))
	result.place(x=80, y=y_axis + 170)


def collect_reg(): #working fine
	clean = Label(root, text="                                                                                                       ")
	clean.place(x=70, y =y_axis+170)
	data= [first.get(),last.get(),username.get(),password.get(),dob.get(),email.get(),phone_no.get()]

	user_file = open("Users_credentials.txt", "a")
	user_file.write(str(data)+"\n")
	user_file.close()

	result = Label(root, text="You are successfully, registered", font=("Calibri", "10"))
	result.place(x=150, y=y_axis + 170)



def regg(): #wroking perfect
	clear_fields()
	#display
	first_.place(x=80, y=y_axis)
	first.place(x=150, y=y_axis)

	last_.place(x=80, y=y_axis + 20)
	last.place(x=150, y=y_axis + 20)

	email_.place(x=80, y=y_axis + 100)
	email.place(x=150, y=y_axis + 100)

	phone_no_.place(x=80, y=y_axis + 120)
	phone_no.place(x=150, y=y_axis + 120)

	login_button.place_forget()
	register_button.place(x=150, y=y_axis + 140)

	clean = Label(root, text="                                                                                                        ")
	clean.place(x=70, y=y_axis+170)


def logg(): #working perfect
	clear_fields()
	login_button.place(x=220, y=y_axis + 140)

	register_button.place_forget()
	first.place_forget()
	last.place_forget()
	email.place_forget()
	phone_no.place_forget()
	first_.place_forget()
	last_.place_forget()
	email_.place_forget()
	phone_no_.place_forget()
	clean = Label(root, text="                                                                                                        ")
	clean.place(x=70, y=y_axis + 170)




y_axis = 60

#DISPLAY
root = Tk()
root.title("Registration and Login")
root.geometry("400x300")

#Main display
heading = Label(root, text="Registration and Login", font=("Calibri", "20"))
heading.place(x=80, y=8)

username = Entry(root)
username_ = Label(root, text="Username")

password = Entry(root)
password_ = Label(root, text="Password")

dob = Entry(root)
dob_ = Label(root, text="Dob")

username_.place(x=80, y=y_axis+ 40)
username.place(x=150, y=y_axis+ 40)

password_.place(x=80, y=y_axis + 60)
password.place(x=150, y=y_axis + 60)

dob_.place(x=80, y=y_axis + 80)
dob.place(x=150, y=y_axis + 80)


login_button = Button(root, text="Login", command=collect_log)
login_button.place(x=220, y=y_axis + 140)




registering = Button(root, text="Register", bd=3, command=regg)
registering.place(x=130, y=y_axis + 200)

or_block = Label(root, text="or", font=("Calibri", "15"))
or_block.place(x=190, y=y_axis + 200)

login = Button(root, text="Login", bd=3, command=logg)
login.place(x=220, y=y_axis + 200)


#registration display start
first = Entry(root)
first_ = Label(root, text="First name")
last = Entry(root)
last_ = Label(root, text="Last name")

email = Entry(root)
email_ = Label(root, text="Email")

phone_no = Entry(root)
phone_no_ = Label(root, text="Phone no.")

register_button = Button(root, text="Register", command=collect_reg)
#registration display end

logg()

root.mainloop()


