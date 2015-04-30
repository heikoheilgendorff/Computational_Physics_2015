# classes
import numpy as nm

class Complex:

	def __init__(self, r=0, i=0):
		self.r=r
		self.i=i
	def copy(self):
		return(Complex(self.r, self.i))
	
	def conj(self):
		ans = self.copy()
		ans.r = ans.r
		ans.i = - ans.i
		return ans

	def __add__(self,val):
		ans = self.copy()
		if isinstance(val,Complex):
			ans.r = ans.r + val.r
			ans.i = ans.i + val.i
		else:
			ans.r = ans.r + val
		return ans

	def __sub__(self,val):
		ans = self.copy()
		if isinstance(val,Complex):
			ans.r = ans.r - val.r
			ans.i = ans.i - val.i
		else:
			ans.r = ans.r - val
		return ans
	
	def __mul__(self,val):
		ans = self.copy()
		ans2 = self.copy()
		if isinstance(val,Complex):
			ans.r = ans.r*val.r - ans.i*val.i
			ans.i = ans2.i*val.r + ans2.r*val.i
		else:
			ans.r = ans.r*val
			ans.i = ans.i*val
		return ans

	def __div__(self,val):
		ans = self.copy()
		if isinstance(val,Complex):
			val2 = val.conj()
			ans = ans*val2/(val.i**2 + val.r**2)	
			
		else:
			ans.r = ans.r/val
			ans.i = ans.i/val
		return ans

	def __repr__(self):
		if (self.i<0):
			return repr(self.r) + ' - ' +repr(-1*self.i)+ 'i'
		else:
			return repr(self.r)+ ' + ' +repr(self.i)+ 'i'
	
	def abs(self):
		return nm.sqrt(self.r**2 + self.i**2)


if __name__=="__main__":
	'''	
	num=Complex()
	print 'real part of num is ' + repr(num.r)
	print 'imaginary part of num is ' + repr(num.i)
	
	num2 = Complex(2,5)
	print 'real part of num2 is ' + repr(num2.r)
	print 'imaginary part of num2 is ' + repr(num2.i)

	myabs = num2.abs()
	print 'absolute value is ' + repr(myabs)

	print num2
	'''
	a = Complex(1.,5.)
	b = a.copy()
	bneg = a.copy()
	bneg.r,bneg.i = -6,-3
	b.r, b.i = 6., 3.
	'''
	print 'a and b are ' + repr(a) + ' and ' + repr(b)
	
	c = a + b
	print 'a + b = ' + repr(c)

	print 'a and b are ' + repr(a) + ' and ' + repr(b)
	c = a - b
	print 'a - b = ' + repr(c)
	'''
	print 'a and b are ' + repr(a) + ' and ' + repr(b)
	c = a * 5
	print ' a * 5 = ' +repr(c)
	c = a * b
	print 'a * b = ' +repr(c)
	d = a * bneg
	print 'a * (-b) = ' +repr(d)

	print 'a and b are ' + repr(a) + ' and ' + repr(b)
	c = a/5.
	print 'a / 5 = ' + repr(c)

	c = a/b
	print 'a/b = ' + repr(c)
	
	









