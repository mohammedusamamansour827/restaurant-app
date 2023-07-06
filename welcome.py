from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys
pro = Tk()
pro.geometry('800x450+280+50')
pro.resizable(TRUE,TRUE)
pro.title('BASMET BARON')
title =Label(pro , text='BASMET BARON System', fg='gold',bg='black',font=('tajawal',20,'bold'))
title.pack(fill=X)

u1='https://www.facebook.com/flafel.basmetbaron?mibextid=LQQJ4d'

u2='https://maps.app.goo.gl/jLyitPwWF8os2YpM7?g_st=ic'

u3='https://instagram.com/flafelbasmetbaron?igshid=YmMyMTA2M2Y='

def Open1():
    webbrowser.open_new(u1)
def Open2():
    webbrowser.open_new(u2)
def Open3():
    webbrowser.open_new(u3)


F1 = Frame(pro , width=230 , height=420 , bg='#0B2F3A')
F1.place(x=570,y=37)
Title1 = Label(F1 , text='مشروع مطعم' , bg='#0B2F3A' , fg='white', font=('tajawal',12,'bold'))
Title1.place(x=75,y=10)
Title2 = Label(F1,text='المطور محمد اسامه', bg='#0B2F3A' , fg='white', font=('tajawal',12,'bold'))
Title2.place(x=55,y=50) 
Title3 = Label(F1 , text='وسائل الاتصال بنا' , bg='#0B2F3A' , fg='white', font=('tajawal',12,'bold'))
Title3.place(x=62,y=90)
B1=Button(F1, text='حسابنا على فيسبوك' ,width=22,fg='BLACK',bg='#DBA901',font=('tajawal / mada', 11,'bold '),command=Open1)
B1.place(x=6,y=130)
B2=Button(F1, text='م وقعنا',width=22,fg='blue',bg='#DBA901',font=('tajawal / mada', 11,'bold '),command=Open2)
B2.place(x=6,y=167)
B3=Button(F1, text='حسابنا على انستاجرام' ,width=22,fg='BLACK',bg='#DBA901',font=('tajawal / mada', 11,'bold '),command=Open3)
B3.place(x=6,y=204)
B4=Button(F1, text='من نحن' ,width=22,fg='BLACK',bg='#DBA901',font=('tajawal / mada', 11,'bold '))
B4.place(x=6,y=242)
B5=Button(F1, text='نبذة عن المطور' ,width=22,fg='BLACK',bg='#DBA901',font=('tajawal / mada', 11,'bold '))
B5.place(x=6,y=279)
B6=Button(F1, text='اغلاق البرنامج' ,width=22,fg='BLACK',bg='#DBA901',font=('tajawal / mada', 11,'bold '),command=quit)
B6.place(x=6,y=317)


photo = PhotoImage(file="D:\\icon.png") 
imo = Label(pro,image=photo)
imo.place(x=120,y=43,width=308,height=272)

F2 = Frame(pro , width=570 ,height=120 , bg='#0B2F3A')
F2.place(x=0, y=330)
photo1 = PhotoImage( file='D:\\pngwing.com (6).png')
imo1 = Label(pro , image=photo1)
imo1.place(x= 450,y= 335, width=110, height=110)
L1 =Label(F2,text='اسم النستخدم', fg='gold',bg='#0B2F3A', font=('tajawal',12))
L1.place(x=330,y=25)
L2 =Label(F2,text='كلمة المرور', fg='gold',bg='#0B2F3A', font=('tajawal',12))
L2.place(x=330,y=70)
En1 = Entry(F2 , font=('tajawal',12), justify='center')
En1.place(x=130,y=26)
En2 = Entry(F2 , font=('tajawal',12), justify='center')
En2.place(x=130,y=71)
B = Button(F2 , text='تسجيل الدخول' ,bg='#DBA901',font=('tajawal',12), width=12 , height=3)
B.place(x=10,y=20)



pro.mainloop()