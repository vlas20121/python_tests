from numpy import zeros, array, linspace
from math import factorial
from matplotlib.pyplot import plot, axes, xlim, ylim
import matplotlib.pyplot as plt

def Interpolation(x,u,a) :
	N = len(x)-1; U = zeros((N+1,N+1))
	for n in range(N+1) :
		U[n,0] = u[n]
	for k in range(1,N+1) :
		for n in range(N+1-k) :
			U[n,k] = k*(U[n,k-1] - U[n+1,k-1])/(x[n] - x[n+k])
	sum = 0.
	for n in range(N+1) :
		mult = 1.
		for k in range(n) :
			mult = mult*(a - x[k])
		sum = sum + U[0,n]/factorial(n)*mult
	return(sum)

x = array([2, 4, 2, 4])
u = array([2, 4, 4, 2])

t = array([2, 4, 3, 1])

plot(x,u,'go',markersize = 7.)
#plt.show()

t_interp = linspace(0,5,100)
u_interp = Interpolation(t,u,t_interp)
x_interp = Interpolation(t,x,t_interp)

plot(x_interp,u_interp,'-r')
xlim((0,10)); ylim((0,6)); 
#axes().set_aspect(1)
plt.show()
# Листинг программы, реализующей
# параметрическую интерполяцию кривой