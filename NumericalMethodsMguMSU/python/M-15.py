﻿#! python3.7
# -*- coding: utf-8 -*- 
from numpy import zeros, linspace
from matplotlib.pyplot import style, figure, axes
from celluloid import Camera

# Набор команд, за счёт которых анимация строится в отдельном окне
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

# Функция f подготавливает массив, содержащий элементы вектор-функции, 
# определяющей правую часть решаемой системы ОДУ 
def f(u,t,m_sun,G) :
	f = zeros(4)
	f[0] = u[2]
	f[1] = u[3]
	f[2] = - G*m_sun*u[0]/(u[0]**2 + u[1]**2)**(3/2)
	f[3] = - G*m_sun*u[1]/(u[0]**2 + u[1]**2)**(3/2)
	return f

# Определение входных данных задачи
t_0 = 0.; T = 365.25*24*60*60
x_0 = 147098291*10**3; y_0 = 0.
v_x_0 = 0.; v_y_0 = 30.4*10**3
G = 6.674301515151515*10**(-11)
m_sun = 1.98847*10**30

# Определение числа интервалов сетки,
# на которой будет искаться приближённое решение 
M = 365

# Определение сетки 
tau = (T - t_0)/M
t = linspace(t_0,T,M + 1)

# Выделение памяти под массив сеточных значений решения системы ОДУ
# В строке с номером m этого массива хранятся сеточные значения решения,
# соответствующие моменту времени t_m
u = zeros((M + 1,4))

# Задание начальных условий
# (записываются в строку с номером 0 массива u)
u[0] = [x_0, y_0, v_x_0, v_y_0]

# Реализация схемы Эйлера
for m in range(M) :
	u[m + 1] = u[m] + tau*f(u[m],t[m],m_sun,G)

# Анимация отрисовки решения 
style.use('dark_background')
fig = figure()
camera = Camera(fig)
ax = axes(xlim=(-2*10**11,2*10**11), ylim=(-2*10**11,2*10**11))
ax.set_aspect('equal'); ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title('Траектория движения Земли')
for m in range(M + 1):
	# Отрисовка в начале координат статичного Солнца
	ax.plot(0,0,'yo',markersize=15)
	# Отрисовка Земли в момент времени t[m]
	ax.plot(u[m,0],u[m,1], color='w', marker='o', markersize=7)
	# Отрисовка пути, пройденного Землёй к моменту времени t[m]
	ax.plot(u[:m+1,0], u[:m+1,1], color='w', ls='--', lw=2)
	camera.snap()
animation = camera.animate(interval=15, repeat=False, blit=True)

# Листинг программы, реализущей решение системы ОДУ
# с помощью схемы Эйлера
# (на примереме моделирования движения Земли вокург Солнца)
# (результатом яляется анимированное тдвижение Земли)
