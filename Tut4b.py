# This is an attempt at a class for nbody

import numpy as nm

class nbody:

	def __init__(self,mass = 0,x_pos = 0, y_pos = 0):
		self.mass = mass
		self.x_pos = x_pos
		self.y_pos = y_pos

	var = {'no_of_particles': 10, 'G': 6.67*10**-11}

	def pot_E(self,m,x,y):
		r = nm.zeros(len(x))
		E_top = nm.zeros(len(r))
		f = nm.ones(len(r))
		E = nm.zeros(len(r))
		k = ()
		for k in range(0,len(m)):
			for i in range(0,len(x)):
				r[i] = nm.sqrt((x[k]-x[i])**2 + (y[k]-y[i])**2)
				if r[i] != 0:
					f[i] = r[i]
			for i in range(0,len(x)):
				E_top[i] = nbody.var['G']*m[k]*m[i]
			for i in range(0,len(x)):
				if r[i] != 0:
					E[i] = E_top[i]/r[i]
			print E.sum()

if __name__=="__main__":

	s = nbody.var['no_of_particles']
	x = nm.random.randint(1,10,size=s)
	y = nm.random.randint(1,10,size=s)
	m = nm.random.randint(1,4,size=s)
	test = nbody(m,x,y)
	
	print 'mass is ' + repr(test.mass)
	print 'x_pos is ' + repr(test.x_pos)
	print 'y_pos is ' + repr(test.y_pos)

	energy = test.pot_E(test.mass,test.x_pos,test.y_pos)



