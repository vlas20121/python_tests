from numpy import zeros, array, linspace, dot, linalg
from matplotlib.pyplot import plot, axes, xlim, ylim
import matplotlib.pyplot as plt

def Integration(x,u) :
	N = len(x) - 1
	int = 0.
	for n in range(1,N+1) :
		int = int + (u[n] + u[n-1])/2*(x[n] - x[n-1])
	return int

def phi(x,k) :
	return x**k

def Approximation(x,u,phi,K,a) :
	N = len(x)-1; A = zeros((K+1,K+1)); B = zeros((K+1,1))
	for m in range(K+1) :
		for k in range(K+1) :
			A[m,k] = Integration(x,phi(x,m)*phi(x,k))
			B[m,0] = Integration(x,phi(x,m)*u)
	C = linalg.solve(A,B)
	sum = 0.
	for k in range(K+1) :
		sum = sum + C[k,0]*phi(a,k)
	return(sum)

x = array([1, 2, 3, 5, 6, 7, 8, 9])
u = array([1, 4, 4, 2, 3, 3, 4, 2])

plot(x,u,'go',markersize = 7)
#plt.show()

a = min(x); b = max(x)
x_0 = (a + b)/2; x = (x - x_0)/((b - a)/2)

K = 7

x_approx = linspace(-1,1,100)
u_approx = Approximation(x,u,phi,K,x_approx)

x_approx = x_approx*((b - a)/2) + (a + b)/2
plot(x_approx,u_approx,'-r')
xlim([0,10]); ylim([0,6]); 
#axes().set_aspect(1)
plt.show()

# Листинг программы, реализующей построение 
# аппроксимирующей функции
