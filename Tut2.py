import numpy as nm
import matplotlib.pyplot as plt


def vc(n):
	x = nm.arange(0,n)
	x = 0.5*nm.pi*x/(n-1)
	return x


def integrate_simple(n):
	dx = nm.pi/2/n
	tot = nm.sum(nm.cos(vc(n)))*dx
	return tot


def integrate_simpson(n):
	dx = nm.pi/2/(n-1)*2
	y = nm.cos(vc(n))
	x_odd = y[1:-1:2]
	x_even = y[2:-1:2]
	tot = nm.sum(x_even)/3 + nm.sum(x_odd)*2/3 + y[0]/6 + y[-1]/6
	tot = tot*dx
	return tot



if __name__=="__main__":

	# Question 1:
	k=vc(10)
	print k
	print 0.5*nm.pi
	
	simple_error = ()
	simpson_error = ()
	
	# Question 2:
	pts = [11,31,101,301,1001]
	for i in pts:
		k = integrate_simple(i)
		err = nm.abs(k-1)
		simple_error= nm.append(simple_error,err)
		print repr(i) + ' points yields: ' + repr(k) + ' with error: ' +repr(err)

	# Question 3:
	x = nm.arange(0,10)
	print x
	print x[0:-1:2] # Takes odd element numbers (offset because elements start at 0, not 1)
	print x[1:-1:2] # Takes even elements, leaving first and last
	
	# Question 4:
	for i in pts:
		k = integrate_simpson(i)
		err = nm.abs(k-1)
		simpson_error= nm.append(simpson_error,err)
		print repr(i) + ' points yields: ' + repr(k) + ' with error: ' +repr(err)

	# Question 5:
	plt.plot(pts,simple_error)
	plt.plot(pts,simpson_error,'r')
	ax=plt.gca()
    	ax.set_yscale('log')
    	ax.set_xscale('log')
    	plt.show()
