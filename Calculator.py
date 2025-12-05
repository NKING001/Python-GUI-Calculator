from tkinter import*

first_number = second_number = Operator = None
def get_digit(digit):
    CURRENT = result_label.cget('text')
    new = CURRENT + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text= '') 

def get_operator(op):
    global first_number, Operator

    first_number = int(result_label['text'])
    Operator = op
    result_label.config(text = '')

def get_result():
    global first_number, second_number, Operator

    second_number = int(result_label['text'])

    if Operator == '+':
        result_label.config(text= str(first_number + second_number))
    elif Operator == '-':
        result_label.config(text= str(first_number - second_number))
    elif Operator == '*':
        result_label.config(text= str(first_number * second_number))
    elif Operator == '/':
        result_label.config(text= str(first_number / second_number))  
    else:
        print('Error')   

def Binary_to_Hex():
    value = result_label.cget("text")
    try:
        decimal_value = int(value, 2)
        hex_value = hex(decimal_value)[2:].upper()
        result_label.config(text=hex_value)
    except:
        result_label.config(text="Error")

def Hex_to_Binary():
    value = result_label.cget("text")
    try:
        decimal_value = int(value, 16)
        bin_value = bin(decimal_value)[2:]
        result_label.config(text=bin_value)
    except:
        result_label.config(text="Error")
                   
np = Tk()
np.title("NIHAR's Calculator")
np.geometry('300x380')
np.resizable(0,0)
np.configure(background='pink')

result_label = Label(np,text=0, bg='Black',fg='White')
result_label.grid(row = 0,column = 0,columnspan=25,pady=(50,25), sticky='w')
result_label.config(font=('verdana',30,'bold'))

btn7 = Button(np,text='7',bg= 'Black',fg='White',height=2,width=5,command=lambda: get_digit(7))
btn7.grid(row=2, column= 0)
btn7.config(font=('verdana',14,'bold'))

btn8 = Button(np,text='8',bg= 'Black',fg='White',height=2,width=5,command=lambda: get_digit(8))
btn8.grid(row=2, column= 1)
btn8.config(font=('verdana',14,'bold'))

btn9 = Button(np,text='9',bg= 'Black',fg='White',height=2,width=5,command=lambda: get_digit(9))
btn9.grid(row=2, column= 2)
btn9.config(font=('verdana',14,'bold'))

btn4 = Button(np,text='4',bg= 'Black',fg='White',height=2,width=5,command=lambda: get_digit(4))
btn4.grid(row=3, column= 0)
btn4.config(font=('verdana',14,'bold'))

btn5 = Button(np,text='5',bg= 'Black',fg='White',height=2,width=5,command=lambda: get_digit(5))
btn5.grid(row=3, column= 1)
btn5.config(font=('verdana',14,'bold'))

btn6 = Button(np,text='6',bg= 'Black',fg='White',height=2,width=5,command=lambda: get_digit(6))
btn6.grid(row=3, column= 2)
btn6.config(font=('verdana',14,'bold'))

btn1 = Button(np,text='1',bg= 'Black',fg='White',height=2,width=5,command=lambda: get_digit(1))
btn1.grid(row=4, column= 0)
btn1.config(font=('verdana',14,'bold'))

btn2 = Button(np,text='2',bg= 'Black',fg='White',height=2,width=5,command=lambda: get_digit(2))
btn2.grid(row=4, column= 1)
btn2.config(font=('verdana',14,'bold'))

btn3 = Button(np,text='3',bg= 'Black',fg='White',height=2,width=5,command=lambda: get_digit(3))
btn3.grid(row=4, column= 2)
btn3.config(font=('verdana',14,'bold'))

btn0 = Button(np,text=0,bg= 'Black',fg='White',height=2,width=5,command=lambda: get_digit(0))
btn0.grid(row=5, column= 1)
btn0.config(font=('verdana',14,'bold'))

btn_add = Button(np,text='+',bg= 'Black',fg='White',height=2,width=5, command=lambda : get_operator('+'))
btn_add.grid(row=2, column= 3)
btn_add.config(font=('verdana',14,'bold'))

btn_sub = Button(np,text='-',bg= 'Black',fg='White',height=2,width=5,command=lambda : get_operator('-'))
btn_sub.grid(row=3, column= 3)
btn_sub.config(font=('verdana',14,'bold'))

btn_mul = Button(np,text='x',bg= 'Black',fg='White',height=2,width=5,command=lambda : get_operator('*'))
btn_mul.grid(row=4, column= 3)
btn_mul.config(font=('verdana',14,'bold'))

btn_div = Button(np,text='/',bg= 'Black',fg='White',height=2,width=5,command=lambda : get_operator('/'))
btn_div.grid(row=5, column= 3)
btn_div.config(font=('verdana',14,'bold'))

btn_clr = Button(np,text='C',bg= 'Black',fg='White',height=2,width=5,command=lambda: clear())
btn_clr.grid(row=5, column= 0)
btn_clr.config(font=('verdana',14,'bold'))

btn_eq = Button(np,text='=',bg= 'Black',fg='White',height=2,width=5,command=get_result)
btn_eq.grid(row=5, column= 2)
btn_eq.config(font=('verdana',14,'bold'))

convert_mb = Menubutton(np, text="Convert", relief=FLAT, bg="black", fg="white")
convert_mb.grid(row=0, column=0, columnspan=4, sticky='nw', padx=10, pady=10)

convert_mb.menu = Menu(convert_mb, tearoff=0)
convert_mb["menu"] = convert_mb.menu

convert_mb.menu.add_command(label="Binary to Hex", command=Binary_to_Hex)
convert_mb.menu.add_command(label="Hex to Binary", command=Hex_to_Binary)


np.mainloop()
