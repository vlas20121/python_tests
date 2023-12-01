from sympy import symbols, zeros, diff

a = symbols('a')
f = (a - 1)*(a - 2)**2*(a - 3)**3

eps = 0.00001

N_max = 50
x = zeros(N_max)

x[0] = 4.

for s in range(3) :
	for n in range(N_max) :
		x[n + 1] = (x[n] - f.subs(a,x[n])/diff(f,a).subs(a,x[n])).evalf()
		if n >= 1 and abs((x[n+1]-x[n])/(1-(x[n+1]-x[n])/(x[n]-x[n-1])))<eps :
			k = n + 1
			break
	p = (1/(1 - (x[k] -x[k-1])/(x[k-1] - x[k-2]))).evalf()
	print('Найден корень x[{0}] = {1} с кратностью {2}'.format(s,x[k],p))
	f = f/pow(a - x[k],p)

# Листинг программы, реализующей решение нелинейного уравнения f(x)=0
# с помощью метода Ньютона
# (в том числе реализовано исключение найденных корней с учётом их кратности) 
