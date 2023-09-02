sender_mail = '1by20ai016@bmsit.in'
password = '3069@Giri'

import smtplib
from tkinter import *
import random
from tkinter import messagebox as msgbx


otp = random.randint(100000,999999)
def mail():
    if entry_02.get() == '':
        msgbx.showinfo("Error","Please enter email")
    else:
        receiver = entry_02.get()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_mail, password)
        server.sendmail(sender_mail, receiver, f'Your OTP is {otp}')
        print('OTP sent successfully')
        server.quit()



def verify():
    if entry_03.get() =='':
        msgbx.showinfo("Error","Please Enter OTP")
    else:
        if entry_03.get() == str(otp):
            lbl.config(text="OTP verified Successfully.")
        else:
            lbl.config(text="Invalid OTP")

gui = Tk()
gui.geometry('500x500')
gui.config(bg='#65a8f0')
gui.title('OTP Verification')

l = Label(gui,text='OTP VERIFICATION',font=("Times",20,"bold"),bg='#65a8f0').place(x=120,y=90)

labl_2 = Label(gui, text="Email :", bg= '#65a8f0', font=("bold", 15))
labl_2.place(x=58, y=180)

entry_02 = Entry(gui,width=20,font=12)
entry_02.place(x=130, y=182)

b = Button(gui, text='Send OTP',width=10,bg='brown',fg='white',command=mail).place(x=360,y=182)

labl_3 = Label(gui, text="OTP :", bg= '#65a8f0', font=("bold", 15))
labl_3.place(x=58, y=280)

entry_03 = Entry(gui,width=10,font=12)
entry_03.place(x=120, y=280)

b = Button(gui, text='Verify',width=10,bg='green',fg='white',command=verify).place(x=240,y=280)

lbl = Label(gui, text = "",bg='#65a8f0',font=18)
lbl.place(x=120,y=350)


gui.mainloop()









