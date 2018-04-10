# Data Analysis
import numpy as np 
import matplotlib.pyplot as plt 
from numpy.fft import fft, fftshift, fftfreq, ifft, ifftshift
import pandas as pd


# path =  '/Users/parham/Dropbox/Tectonic lab/apollo3/Apollo3.3_Dif'
path =  '/Users/tasca/Desktop/Tectonic lab/apollo4/Apollo4_Dif_hilly'

def dock(n, path, comp, dt):
	files = np.arange(1, n+1, dt)
	z = 0
	a = 0
	matrices = []
	for i in files:
		num = '%05d' % i
		name = path + '/B' + num + '.dat' # name of the file to read
		snow = pd.read_csv(name, header = 2, nrows = 1)
		I = int(snow.keys()[1][3:])
		J = int(snow.keys()[2][3:])
		v = np.loadtxt(name, skiprows = 3)
		z = np.transpose(v)[comp] - a
		# a += z
		m = np.reshape(z, [J,I])
		matrices.append(m)

	return matrices

# path =  '/Users/Parham/Dropbox/Tectonic lab/apollo4/A4_1-1300'

num_of_files = 208
Vx = 3
Vy = 4
Vz = 5
dt = 1
time = np.arange(num_of_files)


# X and Y vectors time series
x_1 = np.zeros(num_of_files)
y_1 = np.zeros(num_of_files)
x_2 = np.zeros(num_of_files)
y_2 = np.zeros(num_of_files)
x_3 = np.zeros(num_of_files)
y_3 = np.zeros(num_of_files)


# mx = dock(num_of_files, path , Vx, dt)
my = dock(num_of_files, path, Vy, dt)

for t, i in enumerate(time): 

	# ax1 = np.asarray(mx[i][80:100, 50:75])
	# ax2 = np.asarray(mx[i][80:100, 90:115])
	# ax3 = np.asarray(mx[i][80:100, 140:165])

	ay1 = np.asarray(my[i][50:70, 50:75])
	ay2 = np.asarray(my[i][100:120, 50:75])
	ay3 = np.asarray(my[i][150:170, 50:75])

	# Sum of vectors in each area
	# ax1 = sum(sum(ax1))
	# ax2 = sum(sum(ax2))
	# ax3 = sum(sum(ax3))
	ay1 = sum(sum(ay1))
	ay2 = sum(sum(ay2))
	ay3 = sum(sum(ay3))

	# a1 = np.sqrt(ax1**2 + ay1**2)
	# a2 = np.sqrt(ax2**2 + ay2**2)
	# a3 = np.sqrt(ax3**2 + ay3**2)

	# x_1[t] = ax1
	# x_2[t] = ax2
	# x_3[t] = ax3

	x_1[t] = ay1
	x_2[t] = ay2
	x_3[t] = ay3

z1 = np.polyfit(time, x_1, 1)
z2 = np.polyfit(time, x_2, 1)
z3 = np.polyfit(time, x_3, 1)

trend1 = z1[1] + z1[0]*time
trend2 = z2[1] + z2[0]*time
trend3 = z3[1] + z3[0]*time

# vectors detrended
x_1dt = x_1 - trend1
x_2dt = x_2 - trend2
x_3dt = x_3 - trend3

nom = 'apollo4'
# nom = 'apollo3'

plt.figure()
plt.title('Velocity sum of area in the x-dir')
plt.plot(x_1, label = 'x1')
plt.plot(x_2, label = 'x2')
plt.plot(x_3, label = 'x3')
plt.legend()
plt.savefig('{}_velocity.eps'.format(nom))

plt.figure()
plt.title('Trend of the Velocity data')
plt.plot(trend1, label = 'x1')
plt.plot(trend2, label = 'x2')
plt.plot(trend3, label = 'x3')
plt.legend()
plt.savefig('{}_trend.eps'.format(nom))

plt.figure()
plt.title('Detrended Velocity data')
plt.plot(x_1dt, label = 'x1')
plt.plot(x_2dt, label = 'x2')
plt.plot(x_3dt, label = 'x3')
plt.legend()
plt.savefig('{}_detrended_velocity.eps'.format(nom))


freq = fftshift(fftfreq(num_of_files))

fft_x1 = abs(fftshift(fft(x_1dt)))
fft_x2 = abs(fftshift(fft(x_2dt)))
fft_x3 = abs(fftshift(fft(x_3dt)))

plt.figure()
plt.title('fft of detrended data.eps')
plt.plot(freq, fft_x1, label = 'x1')
plt.plot(freq, fft_x2, label = 'x2')
plt.plot(freq, fft_x3, label = 'x3')
plt.legend()
plt.savefig('{}_fft_detrended.eps'.format(nom))

fft_x1[freq > 0.01] = 0
fft_x1[freq < -0.01] = 0
ifft_x1 = fftshift(ifft(ifftshift(fft_x1)))
fft_x2[freq > 0.01] = 0
fft_x2[freq < -0.01] = 0
ifft_x2 = fftshift(ifft(ifftshift(fft_x2)))
fft_x3[freq > 0.01] = 0
fft_x3[freq < -0.01] = 0
ifft_x3 = fftshift(ifft(ifftshift(fft_x3)))

plt.figure()
plt.title('fft of detrended data with high frequencies removed')
plt.plot(freq, fft_x1, label = 'x1')
plt.plot(freq, fft_x2, label = 'x2')
plt.plot(freq, fft_x3, label = 'x3')
plt.legend()
plt.savefig('{}_fft_nr.eps'.format(nom))

plt.figure()
plt.title('Detrended Velocity model with noise removed')
plt.plot(ifft_x1, label = 'x1')
plt.plot(ifft_x2,label = 'x2')
plt.plot(ifft_x3, label = 'x3')
plt.legend()
plt.savefig('{}_detrended_nr.eps'.format(nom))

plt.figure()
plt.title('Velocity model with noise removed')
plt.plot(ifft_x1 + trend1, label = 'x1')
plt.plot(ifft_x2 + trend2,label = 'x2')
plt.plot(ifft_x3 + trend3, label = 'x3')
plt.legend()
plt.savefig('{}_velocity_nr.eps'.format(nom))


plt.show()
