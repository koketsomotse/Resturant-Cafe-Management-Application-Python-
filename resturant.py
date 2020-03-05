from tkinter import *
import random
import time

root=Tk()
root.geometry("1600x800+0+0")
root.title("Fresh Restaurant Cafe")


text_Input=StringVar()
operator=""
#cont = Canvas(root,width=100,height=120, bg="white")
#cont.grid(row=0,column=0)
#imgLogo=PhotoImage(file="images(1).png")
#image=cont.create_image(80,70,image=imgLogo)


Tops=Frame(root,width=1600,height=50,bg="Orange",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=700,bg="lawn green",relief=SUNKEN)
f2.pack(side=RIGHT)
#=====================TIME==========================#
localtime=time.asctime(time.localtime(time.time()))


#================Info=================================#
lblInfo=Label(Tops,font=('arial',50,'bold'),text="Fresh Restaurant Cafe",fg="DarkOrange2",bd=15,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Orange",bd=15,anchor='w')
lblInfo.grid(row=1,column=0)

#=======================Calculator===================#
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
    

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")


def btnEquals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator=""
    

txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="green",justify="right")
txtDisplay.grid(columnspan=4)
#==================calculator====================#

bt7=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="7",bg='green',command=lambda:btnClick(7)).grid(row=2,column=0)
bt8=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="8",bg='green',command=lambda:btnClick(8)).grid(row=2,column=1)
bt9=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="9",bg='green',command=lambda:btnClick(9)).grid(row=2,column=2)
btAdd=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="+",bg='green',command=lambda:btnClick("+")).grid(row=2,column=3)

bt4=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="4",bg='green',command=lambda:btnClick(4)).grid(row=3,column=0)
bt5=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="5",bg='green',command=lambda:btnClick(5)).grid(row=3,column=1)
bt6=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="6",bg='green',command=lambda:btnClick(6)).grid(row=3,column=2)
btSub=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="-",bg='green',command=lambda:btnClick("-")).grid(row=3,column=3)

bt1=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="1",bg='green',command=lambda:btnClick(1)).grid(row=4,column=0)
bt2=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="2",bg='green',command=lambda:btnClick(2)).grid(row=4,column=1)
bt3=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="3",bg='green',command=lambda:btnClick(3)).grid(row=4,column=2)
btTimes=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="*",bg='green',command=lambda:btnClick("*")).grid(row=4,column=3)

bt0=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="0",bg='green',command=lambda:btnClick(0)).grid(row=5,column=0)
btClear=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),command=btnClearDisplay,text="C",bg='green').grid(row=5,column=1)
btEquals=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),command=btnEquals,text="=",bg='green').grid(row=5,column=2)
btDiv=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="/",bg='green',command=lambda:btnClick("/")).grid(row=5,column=3)

#===========================================================================

rand = StringVar()
Mogodu=StringVar()
Ting=StringVar()
Skopo=StringVar()
Umnqusho=StringVar()
ShisaNyama=StringVar()
Samp=StringVar()
Mashonzha=StringVar()
TotalCost=StringVar()
Pojiekos=StringVar()
ServiceCharge=StringVar()
Mageu=StringVar()

lblReference=Label(f1,font=('arial',16,'bold'),text=" Ref No: ",bd=16,anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="orange red",justify='right')
txtReference.grid(row=0,column=1)


lblMogodu=Label(f1,font=('arial',16,'bold'),text="Mogodu (R35)",bd=16,anchor='w')
lblMogodu.grid(row=1,column=0)
txtMogodu=Entry(f1,font=('arial',16,'bold'),textvariable=Mogodu,bd=10,insertwidth=4,bg="orange red",justify='right')
txtMogodu.grid(row=1,column=1)

lblTing=Label(f1,font=('arial',16,'bold'),text="Ting (R25)",bd=16,anchor='w')
lblTing.grid(row=2,column=0)
txtTing=Entry(f1,font=('arial',16,'bold'),textvariable=Ting,bd=10,insertwidth=4,bg="orange red",justify='right')
txtTing.grid(row=2,column=1)


lblUmnqusho=Label(f1,font=('arial',16,'bold'),text="Umnqusho (R40)",bd=16,anchor='w')
lblUmnqusho.grid(row=3,column=0)
txtUmnqusho=Entry(f1,font=('arial',16,'bold'),textvariable=Umnqusho,bd=10,insertwidth=4,bg="orange red",justify='right')
txtUmnqusho.grid(row=3,column=1)


lblSkopo=Label(f1,font=('arial',16,'bold'),text="Skopo (R35)",bd=16,anchor='w')
lblSkopo.grid(row=4,column=0)
txtSkopo=Entry(f1,font=('arial',16,'bold'),textvariable=Skopo,bd=10,insertwidth=4,bg="orange red",justify='right')
txtSkopo.grid(row=4,column=1)

lblShisaNyama=Label(f1,font=('arial',16,'bold'),text="ShisaNyama (R40)",bd=16,anchor='w')
lblShisaNyama.grid(row=5,column=0)
txtShisaNyama=Entry(f1,font=('arial',16,'bold'),textvariable=ShisaNyama,bd=10,insertwidth=4,bg="orange red",justify='right')
txtShisaNyama.grid(row=5,column=1)


#================================================================================================#

lblSamp=Label(f1,font=('arial',16,'bold'),text="Samp (R55)",bd=16,anchor='w')
lblSamp.grid(row=0,column=2)
txtSamp=Entry(f1,font=('arial',16,'bold'),textvariable=Samp,bd=10,insertwidth=4,bg="red3",justify='right')
txtSamp.grid(row=0,column=3)


lblPojiekos=Label(f1,font=('arial',16,'bold'),text="Pojiekos (R55)",bd=16,anchor='w')
lblPojiekos.grid(row=1,column=2)
txtPojiekos=Entry(f1,font=('arial',16,'bold'),textvariable=Pojiekos,bd=10,insertwidth=4,bg="red3",justify='right')
txtPojiekos.grid(row=1,column=3)




lblMageu=Label(f1,font=('arial',16,'bold'),text="Mageu (R10)",bd=16,anchor='w')
lblMageu.grid(row=2,column=2)
txtMageu=Entry(f1,font=('arial',16,'bold'),textvariable=Mageu,bd=10,insertwidth=4,bg="red3",justify='right')
txtMageu.grid(row=2,column=3)


lblMashonzha=Label(f1,font=('arial',16,'bold'),text="Mashonzha (R15)",bd=16,anchor='w')
lblMashonzha.grid(row=3,column=2)
txtMashonzha=Entry(f1,font=('arial',16,'bold'),textvariable=Mashonzha,bd=10,insertwidth=4,bg="red3",justify='right')
txtMashonzha.grid(row=3,column=3)


lblServiceCharge=Label(f1,font=('arial',16,'bold'),text="Service Charge",bd=16,anchor='w')
lblServiceCharge.grid(row=4,column=2)
txtServiceCharge=Entry(f1,font=('arial',16,'bold'),textvariable=ServiceCharge,bd=10,insertwidth=4,bg="red3",justify='right')
txtServiceCharge.grid(row=4,column=3)

lblTotalCost=Label(f1,font=('arial',16,'bold'),text="Total Cost",bd=16,anchor='w')
lblTotalCost.grid(row=5,column=2)
txtTotalCost=Entry(f1,font=('arial',16,'bold'),textvariable=TotalCost,bd=10,insertwidth=4,bg="red3",justify='right')
txtTotalCost.grid(row=5,column=3)

#=========================Buttons=======================================#

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="gray39").grid(row=9,column=1)
btnTotal=Button(f1,font=('arial',10,'bold'),width=1,text=" ").grid(row=8,column=1)
btnTotal=Button(f1,font=('arial',10,'bold'),width=1,text=" ").grid(row=8,column=2)
btnTotal=Button(f1,font=('arial',10,'bold'),width=1,text=" ").grid(row=8,column=3)
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="gray39").grid(row=9,column=2)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="gray39").grid(row=9,column=3)



root.mainloop()
