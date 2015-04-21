import numpy as nm
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt

def gauss(x,x0=0,sig=1):
	y = nm.exp(-0.5*(x-x0)**2/sig**2)
	return y

def conv(f,g):
	ft1 = fft(f)
	ft2 = fft(g)
	return nm.real(ifft(ft1*ft2))

def conv_shift(x,s):
	k = gauss(x)
	delt = nm.zeros(len(x))
	delt[s] = 1
	c = conv(k,delt)
	return k,c

def cor(f,g):
	ft1 = fft(f)
	ft2 = fft(g)
	con = nm.conj(ft2)
	return nm.real(ifft(ft1*con))

def conv_no_wrap(f,g):
	buff = nm.zeros(100)
	f = nm.append(f, buff)
	#f = nm.append(buff, f)
	g = nm.append(g, buff)
	#g = nm.append(buff, g)
	c = conv(f,g)
	return c

if __name__=="__main__":
	
	# Question 1:

	# Create array:
	x = nm.arange(-10,10,0.1)
	
	# Shift gaussian via convolution:
	a,b = conv_shift(x,len(x)/2)

	plt.plot(a)
	plt.plot(b)
	plt.show()

	# Question 2:
	k = gauss(x)
	c = cor(k,k)
	plt.plot(c)
	plt.show()
	
	
	# Question 3:
	shifts = [1,10,50,len(x)/2]
	col = ['r','g','b','k']
	for i in range(0,len(shifts)):
		a,b = conv_shift(x,shifts[i])
		c = cor(a,b)
		plt.plot(c,col[i])
	plt.show()
	# gaussian moves from right to left as shift position increases
	# Surprised because I was expecting it to follow the shift from 
	# center towards right. Probably didn't think it through...

	# Question 4:
	d = conv_no_wrap(gauss(x),gauss(x))
	plt.plot(d)
	plt.show()








