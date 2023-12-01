from sympy import symbols, zeros, diff, exp

a = symbols('a')
f = exp(a) - 2

eps = 0.0001
k = 0.1

N_max = 50
x = zeros(N_max)

x[0] = -2.

for n in range(N_max) :
	x[n + 1] = (x[n] - f.subs(a,x[n])/diff(f,a).subs(a,x[n])).evalf()
	psi_0 = f.subs(a,x[n])**2 ; psi_1 = f.subs(a,x[n + 1])**2
	tau_n = (psi_0 + k*psi_1)/(psi_0 + psi_1)
	x[n + 1] = (x[n] - tau_n*f.subs(a,x[n])/diff(f,a).subs(a,x[n])).evalf()
	if n >= 1 and abs((x[n+1]-x[n])/(1-(x[n+1]-x[n])/(x[n]-x[n-1])))<eps :
		k = n + 1
		break

print('Найден корень x = {0:.2f}, число итераций - {1}'.format(x[k],k))

# Листинг программы, реализующей решение нелинейного уравнения f(x)=0
# с помощью обобщённого метода Ньютона
