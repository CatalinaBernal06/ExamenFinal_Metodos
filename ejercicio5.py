# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sig = 10
beta = 2.67
rho = 28.0
t = 0
x = 0.0
y = 0.0
z = 0.0
delta_t = 0.001
delta_x = 0.01
T_max = 5.0

def dx_dt(x, y):
    return sig * (y - x)

def dy_dt(x, y, z):
    return rho * x - y - x*z

def dz_dt(x, y, z):
    return -beta * z + x * y

x_l = list()
y_l = list()
z_l = list()

while(t<T_max):
    xi = dx_dt(x, y)
    x_l.append(xi)
    yi = dy_dt(x, y, z)
    y_l.append(yi)
    zi = dz_dt(x, y, z)
    z_l.append(zi)

    t += delta_t
    x += xi
    y += yi
    z += zi
    
    
plt.figure()
plt.plot(x_l, y_l, label ='xy')
plt.title('x vs. y')
plt.legend()
plt.savefig('xy.png')

plt.figure()
plt.plot(x_l, z_l, label='xz')
plt.title('x vs. z')
plt.legend()
plt.savefig('xz.png')
