from numpy import zeros

def f(x) :
	return (x - 1)*(x - 2)**2*(x - 3)**3

eps = 0.1

N_max = 50
x = zeros(N_max)

x[0] = 2.5
x[1] = 3.6

n = 1
while abs(x[n] - x[n-1]) > eps :
	x[n+1] = (x[n] + x[n-1])/2
	if f(x[n+1])*f(x[n-1]) < 0:
		x[n] = x[n-1]
	elif f(x[n+1]) == 0 :
		n = n + 1
		break
	n = n + 1

print('Найден корень x = {0:.2f}, число итераций - {1}'.format(x[n],n-1))

# Листинг программы, реализующей решение нелинейного уравнения f(x)=0
# с помощью метода дихотомии (метод деления отрезка пополам)
