'''
Functions used to serve MissionControl.py of the KENNEDY package. Functions used to import files into python, and 
create different plots with the data.

Created by Parham Adiban.
June 19, 2017
'''

from numpy import *
import matplotlib.pyplot as plt
import tkMessageBox
import pandas as pd

def dock(n, path, comp, dt):
	files = arange(1, n+1, dt)
	z = 0
	a = 0
	matrices = []
	for i in files:
		num = '%05d' % i
		name = path + '/B' + num + '.dat' # name of the file to read
		snow = pd.read_csv(name, header = 2, nrows = 1)
		I = int(snow.keys()[1][3:])
		J = int(snow.keys()[2][3:])
		
		v = loadtxt(name, skiprows = 3)
		z = transpose(v)[comp] - a
		# a += z
		m = reshape(z, [J,I])*1000
		matrices.append(m)

	return matrices

def plotrow(n, path, comp, row, dt, PtoM, v):
	mat = dock(n, path, comp, dt)
	plt.figure()
	for t, m in enumerate(mat):
		l =  arange(len(m[row]))*PtoM # length of row
		plt.title('{0} plot at y = {1}mm'.format(v, row*PtoM))
		plt.plot(l, m[row], label = t) # plot specificed row
		plt.ylabel('Velocity (mm/s)')
		plt.xlabel('mm')
	plt.show()

def plotcol(n, path, comp, col, dt, PtoM, v):
	mat = dock(n, path, comp, dt)
	plt.figure()
	for t, m in enumerate(mat):
		l =  arange(len(m[:, col]))*PtoM # length of column
		plt.title('{0} plot at x = {1}mm'.format(v, col*PtoM))
		plt.plot(l, m[:, col], label = t) # plot specificed column
		plt.ylabel('Velocity (mm/s)')
		plt.xlabel('mm')
	plt.show()

def animation(n, path, comp, dt, v_min, v_max, row, col, interval, PtoM, v, StoM):
	mat = dock(n, path, comp, dt)
	fig = plt.figure()
	for t, m in enumerate(mat):
		fig.clear()
		lr = arange(len(m[row]))*PtoM
		lc =  arange(len(m[:, col]))*PtoM
		plt.imshow(m, vmin = v_min, vmax = v_max, extent = [0, lr[-1], 0, lc[-1]])
		plt.title('Time = {0}s = {1}Myr'.format((t-1)*interval*dt, (t-1)*interval*dt//(StoM/3600)))
		plt.gca().invert_yaxis()
		plt.colorbar().ax.set_ylabel('{} (mm/s)'.format(v), rotation=270)
		plt.pause(0.001)
	plt.legend()
	plt.show()

def grad(n, path, comp, dt, v_min, v_max, row, col, interval, PtoM, v, StoM):
	mat = dock(n, path, comp, dt)
	fig = plt.figure()
	for t, m in enumerate(mat):
		fig.clear()
		lr = arange(len(m[row]))*PtoM
		lc =  arange(len(m[:, col]))*PtoM
		plt.imshow(gradient(m)[0], vmin = v_min, vmax = v_max, extent = [0, lr[-1], 0, lc[-1]])
		plt.title('Time = {0}s = {1}Myr'.format((t-1)*interval*dt, (t-1)*interval*dt//(StoM/3600)))
		plt.gca().invert_yaxis()
		plt.colorbar().ax.set_ylabel('{} (mm/s)'.format(v), rotation=270)
		plt.pause(0.001)
	plt.legend()
	plt.show()

def colormap(n, path, comp, dt, v_min, v_max, row, col, direction, PtoM, v):
	mat = dock(n, path, comp, dt)
	fig = plt.figure()
	Row = []
	Col = []

	for m in mat:
		Row.append(m[row])
		Col.append(m[:, col])
		lr = arange(len(m[row]))*PtoM
		lc =  arange(len(m[:, col]))*PtoM

	if direction == 0:
		plt.imshow(Row[::-1],vmin = v_min, vmax = v_max, extent=[0, lr[-1], 0, n])
		plt.title('y = {0}mm'.format(row))

		plt.ylabel('File number')
		plt.xlabel('mm')
		plt.colorbar().ax.set_ylabel('{} (mm/s)'.format(v), rotation=270)

		plt.show()

	if direction == 1:
		plt.imshow(Col[::-1], vmin = v_min, vmax = v_max, extent=[0, lc[-1], 0, n])
		plt.ylabel('File number')
		plt.xlabel('mm')
		plt.title('x = {0}mm'.format(col))
		plt.colorbar().ax.set_ylabel('{} (mm/s)'.format(v), rotation=270)

		plt.show()












