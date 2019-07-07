from tkinter import *
window  = Tk()
window.title("Calculator")

textentry = StringVar()
operator = ""
textentry.set("")

def Enter(val):
    global operator
    operator = operator+str(val)
    textentry.set(operator)

def clear():
    global operator
    operator=""
    textentry.set(operator)

def equals():
    global operator
    sumup=str(eval(operator))
    textentry.set(sumup)
    operator=sumup

Entry(window, font=('arial', 20, 'bold'), textvariable=textentry, insertwidth=4, bg="powder blue", bd=30) .grid(columnspan=4)

btn7 = Button(window, text="7", command=lambda:Enter(7), padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btn7.grid(row=1, column=0)
btn8 = Button(window, text="8", command=lambda:Enter(8), padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btn8.grid(row=1, column=1)
btn9 = Button(window, text="9", command=lambda:Enter(9), padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btn9.grid(row=1, column=2)
btn_div = Button(window, text="/", command=lambda:Enter("/"), padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btn_div.grid(row=1, column=3)
###############################################################
btn4 = Button(window, text="4", command=lambda:Enter(4), padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btn4.grid(row=2, column=0)
btn5 = Button(window, text="5", command=lambda:Enter(5), padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btn5.grid(row=2, column=1)
btn6 = Button(window, text="6", command=lambda:Enter(6), padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btn6.grid(row=2, column=2)
btn_mul = Button(window, text="*", command=lambda:Enter("*"), padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btn_mul.grid(row=2, column=3)
###############################################################
btn1 = Button(window, text="1", command=lambda:Enter(1), padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btn1.grid(row=3, column=0)
btn2 = Button(window, text="2", command=lambda:Enter(2), padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btn2.grid(row=3, column=1)
btn3 = Button(window, text="3", command=lambda:Enter(3), padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btn3.grid(row=3, column=2)
btn_add = Button(window, text="+", command=lambda:Enter("+"), padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btn_add.grid(row=3, column=3)
###############################################################
btn0 = Button(window, text="0", command=lambda:Enter(0), padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btn0.grid(row=4, column=0)
btnc = Button(window, text="C", command=clear, padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btnc.grid(row=4, column=1)
btnequal = Button(window, text="=", command=equals, padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btnequal.grid(row=4, column=2)
btn_min = Button(window, text="-", command=lambda:Enter("-"), padx=30, pady=16, bd=8, font=('arial', 20, 'bold'))
btn_min.grid(row=4, column=3)
###############################################################
window.mainloop()