'''
GUI application created to read .DAT files exported by davis software after 3D surface flow rendering

Created by Parham Adiban.
June 19, 2017

'''

from Tkinter import *
from Houston import *
import tkMessageBox
import tkFileDialog as filedialog

# def openfile():
# 	pathname = filedialog.askdirectory()
# 	var.set(pathname)

def submission():

	while True:
		try:
			path = var.get()
			n = int(n_of_files_.get())
			dt = int(step_.get())
			row = int(rowNum_.get())
			col = int(colNum_.get())
			minimum = float(v_min_.get())
			maximum = float(v_max_.get())
			minimum2 = float(v_min2_.get())
			maximum2 = float(v_max2_.get())
			Interval = int(interval_.get())
			PTOM = float(ptom_.get())
			STOM = float(stom_.get())
			V = var.get()
			if V == 'Vx': 
				comp = 3
			elif V == 'Vy': 
				comp = 4
			elif V == 'Vz': 
				comp = 5

			I = horv.get()
			if I == 'H': 
				Dirn = 0
			elif I == 'V': 
				Dirn = 1

			OPT = opt.get()

			if OPT == 'Colormap':
				colormap(n, path, comp, dt, minimum, maximum, row, col, Dirn, PTOM, V)
			elif OPT == 'plotCol':
				plotcol(n, path, comp, col,dt, PTOM, V)
			elif OPT == 'plotRow':
				plotrow(n, path, comp, row, dt, PTOM, V)
			elif OPT == 'Animate':
				animation(n, path, comp, dt, minimum, maximum, row, col, Interval, PTOM, V, STOM)
			elif OPT == 'Gradient':
				grad(n, path, comp, dt, minimum2, maximum2, row, col, Interval, PTOM, V, STOM)
			break

		except ValueError:
			tkMessageBox.showinfo('Value Error', 'Make sure all numbers are placed correctly!')
			break
		except NameError:
			tkMessageBox.showinfo('Name Error', 'You forgot to put the file path you silly goose.')
			break


def Reset():
	n = n_of_files_.delete(0, 'end')
	dt = step_.delete(0, 'end')
	row = rowNum_.delete(0, 'end')
	col = colNum_.delete(0, 'end')
	minimum = v_min_.delete(0, 'end')
	maximum = v_max_.delete(0, 'end')
	minimum2 = v_min2_.delete(0, 'end')
	maximum2 = v_max2_.delete(0, 'end')
	ptom = ptom_.delete(0, 'end')
	var.set('')	


root = Tk()

roof = Frame(root)
roof.pack()
# filePath = Button(roof, text="Open File Path", width = 10, command=openfile)
# filePath.grid(row = 0, column = 0, columnspan = 2)

var = StringVar()
v = OptionMenu(roof,var,'Vx','Vy','Vz')
v.grid(row = 0, column = 1, sticky = W)

horv = StringVar()
h = OptionMenu(roof,horv,'H','V')
h.grid(row = 0, column = 2, sticky = W)

opt = StringVar()
op = OptionMenu(roof,opt,'Colormap','plotCol', 'plotRow', 'Animate', 'Gradient')
op.grid(row = 0, column = 3, sticky = W)

n_of_files = Label(roof, text = 'File count:')
n_of_files_ = Entry(roof, width = 4)
n_of_files.grid(row = 1, column = 0, sticky = E)
n_of_files_.grid(row = 1, column = 1)


step = Label(roof, text = 'Step:')
step_ = Entry(roof, width = 4)
step.grid(row = 1, column = 2, sticky = E)
step_.grid(row = 1, column = 3, sticky = W)


interval = Label(roof, text = 'Interval:')
interval_ = Entry(roof, width = 4)
interval.grid(row = 1, column = 4, sticky = E)
interval_.grid(row = 1, column = 5, sticky = W)

rowNum = Label(roof, text = 'Row:')
rowNum_ = Entry(roof, width = 4)
rowNum.grid(row = 2, column = 0, sticky = E)
rowNum_.grid(row = 2, column = 1)

colNum = Label(roof, text = 'Column:')
colNum_ = Entry(roof, width = 4)
colNum.grid(row = 2, column = 2, sticky = E)
colNum_.grid(row = 2, column = 3, sticky = W)

ptom = Label(roof, text = '1 mm = ')
ptom2 = Label(roof, text = 'pixel')
ptom_ = Entry(roof, width = 4)
ptom.grid(row = 5, column = 0, sticky = E)
ptom_.grid(row = 5, column = 1, sticky = W)
ptom2.grid(row = 5, column = 2, sticky = W)

stom = Label(roof, text = '1 hr = ')
stom2 = Label(roof, text = 'Myr')
stom_ = Entry(roof, width = 4)
stom.grid(row = 5, column = 3, sticky = E)
stom_.grid(row = 5, column = 4, sticky = W)
stom2.grid(row = 5, column = 5, sticky = W)


Animation = Label(roof, text= 'Animation')
Animation.grid(row = 3, column = 0, columnspan = 2)
v_min = Label(roof, text= 'Min:')
v_max = Label(roof, text= 'Max:')
v_min_ = Entry(roof, width = 4)
v_max_ = Entry(roof, width = 4)

v_min.grid(row = 3, column = 2, sticky = E)
v_min_.grid(row = 3, column = 3, sticky = W)
v_max.grid(row = 3, column = 4, sticky = E)
v_max_.grid(row = 3, column = 5, sticky = W)

Gradient = Label(roof, text= 'Gradient')
Gradient.grid(row = 4, column = 0, columnspan = 2)
v_min2 = Label(roof, text= 'Min:')
v_max2 = Label(roof, text= 'Max:')
v_min2_ = Entry(roof, width = 4)
v_max2_ = Entry(roof, width = 4)

v_min2.grid(row = 4, column = 2, sticky = E)
v_min2_.grid(row = 4, column = 3, sticky = W)
v_max2.grid(row = 4, column = 4, sticky = E)
v_max2_.grid(row = 4, column = 5, sticky = W)

pathname = Entry(roof, width = 16)
pathname.grid(row = 6, column = 0, columnspan = 8)

ground = Frame(root)
ground.pack(side = BOTTOM)

submit = Button(ground, text = 'SUBMIT', command = submission)
reset = Button(ground, text = 'RESET', command = Reset)
quit = Button(ground, text = 'QUIT', command = root.quit)
submit.pack(side = LEFT)
reset.pack(side = LEFT)
quit.pack(side = LEFT)

mid = Frame(root)
mid.pack(side = BOTTOM)

root.mainloop()