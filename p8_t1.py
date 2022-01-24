import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 

t = np.arange(0, 10**2, 10)
 

def radio_function(m, t):
    dmdt =  k*m
    return dmdt
 

m_0 = 10
k = 10
 

solve_Bi = odeint(radio_function, m_0, t)

# Построение решения в виде графика функции
plt.plot(t, solve_Bi[:,0], label='Распад Урана 238')
plt.xlabel('Период распада, секунды')
plt.ylabel('Функция распада')
plt.title('Радиоактивный распад')
plt.legend()

plt.show()
