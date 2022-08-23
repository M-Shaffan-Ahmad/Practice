###DISPLAY###
import Text2Speech_back as t
from tkinter import *


root = Tk()
root.title("Text to Speech")
root.geometry("250x300")

################
Title= Label(root, text="Text to Speech",font=("Calibri",20 ))
Title.place(x=12, y= 20)
###############
text_input=Entry(root, font=("Vareenes",10 ))
text_input.place(x=15, y=80, width =220)
################
play=Button(root, text="PLAY", command=lambda : t.dis(text_input.get()))
play.place(x=100, y = 110)
################
save_name=Entry(root)
save_button=Button(root,text="Save", command=lambda : t.save(save_name.get(), text_input.get()))
save_name.place(x=110 ,y=200)
save_button.place(x=150 ,y=220)
################
Volume=Label(root, text="VOLUME")
Volume.place(x=28, y=150)
volume_low=Button(root, text=" - ", command=t.volume_d)
volume_low.place(x=5, y= 150)
volume_high=Button(root, text=" + ", command=t.volume_u)
volume_high.place(x=82, y= 150)
###############
Rate=Label(root, text="RATE")
Rate.place(x=142, y=150)
rate_low=Button(root, text=" - ", command=t.rate_d)
rate_low.place(x=122, y= 150)
rate_high=Button(root, text=" + ", command=t.rate_u)
rate_high.place(x=175, y= 150)
############
voice_ma= Button(root, text="VOICE_MAlE", command=t.voice_m)
voice_fe= Button(root, text="VOICE_FEMAlE", command=t.voice_f)
voice_fe.place(x=10, y=200)
voice_ma.place(x=10, y=230)
############
root.mainloop()

