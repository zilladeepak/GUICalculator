import math
from tkinter import *
#from tkinter import ttk
import tkinter.font as font
root=Tk()
root.title("Calculator")
root.geometry("570x600")
root.resizable(False,False)
root.configure(bg='#17161b') 

#e=Entry(root, width=70, bg="light grey", fg="black")


e=Entry(root,width=25,font=("arial",30))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=25)
#label.pack()

buttonFont = font.Font(size=20,family='arial',weight='bold')

#e.insert(0,"Enter The Number: ")

#equation=""

def click (number):
    #global equation
    #equation+=number
    num1=e.get()
    e.delete(0,END)
    e.insert(0,str(num1)+str(number))
    
    #   hello="Hello "+e.get()
  #  label=Label(root,text=hello)
   # label.pack()
def clear():
    e.delete(0,END)
    
def add():
    one_num=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(one_num)
    e.delete(0,END)

def div():
    one_num=e.get()
    global f_num
    global math
    math="division"
    f_num=int(one_num)
    e.delete(0,END)

def sub():
    one_num=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(one_num)
    e.delete(0,END)
    
def mul():
    one_num=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(one_num)
    e.delete(0,END)
    
def percent():
    one_num=e.get()
    global f_num
    global math
    math="percent"
    f_num=int(one_num)
    e.delete(0,END)
    
def squ():
    one_num=e.get()
    global f_num
    global math
    math="squ"
    f_num=int(one_num)
    e.delete(0,END)
    
def expo():
    one_num=e.get()
    global f_num
    global math
    math="expo"
    f_num=int(one_num)
    e.delete(0,END)
  
    
def equal():
    
    if math=="addition":
        sc_num=e.get()
        e.delete(0,END)
        e.insert(0,f_num+int(sc_num))
    if math=="subtraction":
        sc_num=e.get()
        e.delete(0,END)
        e.insert(0,f_num-int(sc_num))
    if math=="multiplication":
        sc_num=e.get()
        e.delete(0,END)
        e.insert(0,f_num*int(sc_num))
    if math=="division":
        sc_num=e.get()
        e.delete(0,END)
        e.insert(0,f_num/int(sc_num))
    if math=="percent":
        sc_num=e.get()
        e.delete(0,END)
        e.insert(0,(int(sc_num)*(f_num/100)))
    if math=="squ":
        #sc_num=e.get()
        #e.delete(0,END)
        e.insert(0,(f_num*f_num))
    if math=="expo":
        sc_num=e.get()
        e.delete(0,END)
        e.insert(0,(f_num**int(sc_num)))
     

    
    
buttonclear=Button(root, text="C", bg="#3697f5",fg="#fff",font=buttonFont,bd=1,padx=45,pady=20,command=clear)   
buttonper =Button(root, text="%", bg="#2a2d36",fg="#fff", font= buttonFont, padx=40,pady=20,command=percent)
buttonmul=Button(root, text="X", bg="#2a2d36",fg="#fff",font= buttonFont,padx=45,bd=1,pady=20,command=mul)
buttondiv =Button(root, text="/", bg="#2a2d36",fg="#fff",font= buttonFont,bd=1, padx=47,pady=20,command=div)

button7=Button(root, text="7", bg="#2a2d36",fg="#fff",font=buttonFont,bd=1,padx=45,pady=20,command=lambda: click(7))
button8=Button(root, text="8", bg="#2a2d36",fg="#fff",font=buttonFont,bd=1,padx=45,pady=20,command=lambda: click(8))
button9=Button(root, text="9", bg="#2a2d36",fg="#fff",font=buttonFont,bd=1,padx=45,pady=20,command=lambda: click(9))
buttonsub=Button(root, text="-",bg="#2a2d36",fg="#fff",font=buttonFont,bd=1,padx=49,pady=20,command=sub)


button4=Button(root, text="4", bg="#2a2d36",fg="#fff",font=buttonFont,bd=1,padx=45,pady=20,command=lambda: click(4))
button5=Button(root, text="5", bg="#2a2d36",fg="#fff",font=buttonFont,bd=1,padx=45,pady=20,command=lambda: click(5))
button6=Button(root, text="6", bg="#2a2d36",fg="#fff",font=buttonFont,bd=1,padx=45,pady=20,command=lambda: click(6))
buttonadd=Button(root, text="+",bg="#2a2d36",fg="#fff",font=buttonFont,bd=1,padx=45,pady=20,command=add)



button1=Button(root, text="1", bg="#2a2d36",fg="#fff",font=buttonFont,bd=1,padx=45,pady=20,command=lambda: click(1))
button2=Button(root, text="2", bg="#2a2d36",fg="#fff",font=buttonFont,bd=1,padx=45,pady=20,command=lambda: click(2))
button3=Button(root, text="3", bg="#2a2d36",fg="#fff",font=buttonFont,bd=1,padx=45,pady=20,command=lambda: click(3))



button0=Button(root, text="0", bg="#2a2d36",fg="#fff",font=buttonFont,bd=1,padx=45,pady=20,command=lambda: click(0))
buttonsqu=Button(root, text="x^2", bg="#2a2d36",fg="#fff",font=buttonFont,bd=1,padx=30,pady=20,command=squ)
buttonexpo=Button(root, text="x^y",bg="#2a2d36",fg="#fff",font=buttonFont,bd=1,padx=30,pady=20,command=expo)
buttonequal=Button(root, text="=",bg="#fe9037",fg="#fff",font=buttonFont,bd=1,padx=45,pady=70,command=equal)
   



buttondiv.grid(row=1,column=1)
buttonmul.grid(row=1,column=2)
buttonper.grid(row=1,column=3)
buttonclear.grid(row=1,column=0)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
buttonsub.grid(row=2,column=3)

button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
buttonadd.grid(row=3,column=3)

button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)

button0.grid(row=5,column=1)
buttonsqu.grid(row=5,column=2)
buttonexpo.grid(row=5,column=0)


buttonequal.grid(row=4,column=3,rowspan=2)
   
    
root.mainloop()
