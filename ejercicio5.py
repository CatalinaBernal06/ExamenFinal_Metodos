# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 


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








