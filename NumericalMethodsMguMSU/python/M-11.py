from numpy import linspace, zeros, log, exp
from matplotlib.pyplot import plot, xscale, yscale
import matplotlib.pyplot as plt

def u(x) :
	return exp(x)

def Differentiation(u,x,h):
	dif = (u(x) - u(x - h))/h
	return dif

x = 0.

h = 0.1
r = 2; S = 5
p = 1; q = 1

D = zeros((S,S))
R = zeros((S,S))
p_eff = zeros((S,S))

for s in range(S) :
	D[s,0] = Differentiation(u,x,h/r**s)

for s in range(1,S) :
	for l in range(s) :
		R[s,l] = (D[s,l] - D[s-1,l])/(r**(p + l*q) - 1)
		D[s,l+1] = D[s,l] + R[s,l]

for s in range(2,S) :
	for l in range(s-1) :
		p_eff[s,l] = log(abs(R[s-1,l]/R[s,l]))/log(r)

# Функция выводит форматированную таблицу
def PrintTriangular(A,i) :
	print(' ',end=' ')
	for l in range(len(A)) :
		print(' p={0:<4d}'.format(p + l*q),end=' ')
	print()
	for m in range(len(A)) :
		print('s={0:<2d}'.format(m),end=' ')
		for l in range(m + 1 - i) :
			print('{0:7.4f}'.format(A[m,l]),end=' ')
		print()
	print()

print('Таблица приближённых значений интеграла:')
PrintTriangular(D,0)
print('Таблица оценок ошибок:')
PrintTriangular(R,1)
print('Таблица эффективных порядков точности:')
PrintTriangular(p_eff,2)

plot([r**s*(1- 0)/h for s in range(1,S)],abs(R[1:,0]),'-bo')
xscale('log'); yscale('log')
plt.show()

# Листинг программы, реализущей приближённое вычисление производной
# с помощью рекурретного сгущения сеток и многократного повышения
# точности по Ричардсону (с вычислением эффективных порядков точности)