from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Calculator")

def calc(key):
	global memory

	if key == "=":
		str1 = "-+0123456789.*/"
		if calc_entery.get()[0] not in str1:
			calc_entery.insert(END, "It Is Not Number!" )
			messagebox.showerror( "ERROR!" )

		try:
			result = eval(calc_entery.get())
			calc_entery.insert(END, "="+str(result))

		except:
			calc_entery.insert(END, "ERROR" )
			messagebox.showerror( "ERROR" )

	elif key == "C":
		calc_entery.delete(0, END)

	else:
		if "=" in calc_entery.get():
			calc_entery.delete(0, END)
		calc_entery.insert(END, key)

buttn_list = [
	"7", "8", "9", "C", "=",
	"4", "5", "6", "+", "-",
	"1", "2", "3", "*", "/",
	"0"
]

r = 1
c = 0

for i in buttn_list:
	rel = ""
	cmd = lambda x = i: calc(x)
	ttk.Button(root, text = i, command = cmd) .grid(row = r, column = c)
	c += 1
	if c>4:
		c = 0
		r += 1

calc_entery = Entry(root, width = 45)
calc_entery.grid(row = 0, column = 0, columnspan = 5)

root.mainloop()