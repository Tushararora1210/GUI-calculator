from tkinter import *
root=Tk(className=" CALCULATOR DESIGNED BY TUSHAR ARORA(16802007)")
root.geometry( "800x600" )
Label(root,text="CALCULATOR DESIGNED BY TUSHAR",font=("Courier New",30,'bold')).grid(row=0,column=0)
operator=""
def chk(o):
    o=str(o)
    global operator
    if((o!='=')and(o!='.')):
        operator=operator+o
        textin.set(operator)
    elif(o=='.'):
        textin.set("")
        operator=""
    else:
        if'+' in operator:
            for s in range(0,len(operator)):
                if (operator[s]=='+'):
                    break;
            res=int(operator[0:s])+int(operator[s+1:len(operator)])
            textin.set(res)
        elif '-' in operator:
            for s in range(0, len(operator)):
                if (operator[s] == '-'):
                    break;
            res = int(operator[0:s]) - int(operator[s + 1:len(operator)])
            textin.set(res)
        elif '/' in operator:
            for s in range(0, len(operator)):
                if (operator[s] == '/'):
                    break;
            res = int(operator[0:s]) / int(operator[s + 1:len(operator)])
            textin.set(res)
        elif '*' in operator:
            for s in range(0, len(operator)):
                if (operator[s] == '*'):
                    break;
            res = int(operator[0:s]) * int(operator[s + 1:len(operator)])
            textin.set(res)
        else:
            textin.set("ERROR")
        operator=str(res)





textin=StringVar()
Entry(root,textvar=textin).place(x=90,y=50,width=350,height=40)
Button(root,text='1',bg="Red",padx=14,pady=14,command=lambda:chk(1)).place(x=100,y=100)
Button(root,text='2',bg="Red",padx=14,pady=14,command=lambda:chk(2)).place(x=200,y=100)
Button(root,text='3',bg="Red",padx=14,pady=14,command=lambda:chk(3)).place(x=300,y=100)
Button(root,text='+',bg="Red",padx=14,pady=14,command=lambda:chk('+')).place(x=400,y=100)
Button(root,text='4',bg="Red",padx=14,pady=14,command=lambda:chk(4)).place(x=100,y=200)
Button(root,text='5',bg="Red",padx=14,pady=14,command=lambda:chk(5)).place(x=200,y=200)
Button(root,text='6',bg="Red",padx=14,pady=14,command=lambda:chk(6)).place(x=300,y=200)
Button(root,text='-',bg="Red",padx=14,pady=14,command=lambda:chk('-')).place(x=400,y=200)
Button(root,text='7',bg="Red",padx=14,pady=14,command=lambda:chk(7)).place(x=100,y=300)
Button(root,text='8',bg="Red",padx=14,pady=14,command=lambda:chk(8)).place(x=200,y=300)
Button(root,text='9',bg="Red",padx=14,pady=14,command=lambda:chk(9)).place(x=300,y=300)
Button(root,text='*',bg="Red",padx=14,pady=14,command=lambda:chk('*')).place(x=400,y=300)
Button(root,text='0',bg="Red",padx=14,pady=14,command=lambda:chk(0)).place(x=100,y=400)
Button(root,text="CLR",bg="Red",padx=14,pady=14,command=lambda:chk('.')).place(x=200,y=400)
Button(root,text='=',bg="Red",padx=14,pady=14,command=lambda:chk('=')).place(x=300,y=400)
Button(root,text='/',bg="Red",padx=14,pady=14,command=lambda:chk('/')).place(x=400,y=400)
root.mainloop()
