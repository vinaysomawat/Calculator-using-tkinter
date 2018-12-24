from tkinter import *

expression = ""

def press(num):

		global expression
		expression = expression+str(num)
		equation.set(expression)

def equalpress():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression =""

	except:
		equation.set("Error")
		expression = ""

def clearpress():

		global expression
		expression = ""
		equation.set("")
	
if __name__ =="__main__":
	gui = Tk()

	gui.configure(background = "light green")
	gui.title("Calculator")
	gui.geometry("465x225")
	
	equation = StringVar()

	expression_field= Entry(gui, textvariable= equation)
	expression_field.grid(columnspan = 10,ipadx =70)

	equation.set('enter your expression')

	button0 = Button(gui, text="0", bg="white", fg="black", command= lambda :press(0), height=1, width=7)
	button0.grid(row=5,column=0)

	button1 = Button(gui, text="1", bg="white", fg="black", command=lambda : press(1), height=1, width=7) 
	button1.grid(row=2, column=0)

	button2 = Button(gui, text="2", bg="white", fg="black", command=lambda :press(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text="3", bg="white", fg="black", command=lambda :press(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text="4", bg="white", fg="black", command=lambda :press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text="5", bg="white", fg="black", command=lambda :press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text="6", bg="white", fg="black", command=lambda :press(6), height=1, width=7)
	button3.grid(row=3, column=2)

	button7 = Button(gui, text="7", bg="white", fg="black", command=lambda :press(7), height=1, width=7)
	button4.grid(row=4, column=0)

	button8 = Button(gui, text="8", bg="white", fg="black", command=lambda :press(8), height=1, width=7)
	button5.grid(row=4, column=1)

	button9 = Button(gui, text="9", bg="white", fg="black", command=lambda :press(9), height=1, width=7)
	button3.grid(row=4, column=2)

	plus = Button(gui, text="+", bg="white", fg="black", comman=lambda:press("+"), height=1, width =7)
	plus.grid(row=2, column=3)

	minus = Button(gui, text="-", bg="white", fg="black", comman=lambda:press("-"), height=1, width =7)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text="*", bg="white", fg="black", comman=lambda:press("*"), height=1, width =7)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text="/", bg="white", fg="black", comman=lambda:press("/"), height=1, width =7)
	divide.grid(row=5, column=2)

	equal = Button(gui, text="=", bg="white", fg="black", comman=equalpress, height=1, width =7)
	plus.grid(row=5, column=5)

	clear = Button(gui, text="clear", bg="white", fg="black", comman=clearpress, height=1, width =7)
	plus.grid(row=5, column=4)

	gui.mainloop()

