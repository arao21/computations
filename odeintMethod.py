import numpy as np
import math
import sympy as sym
from sympy import *
from numpy import matrix
from numpy import linalg
from sympy import MatrixSymbol, Matrix
from numpy.linalg import inv
from matplotlib import pyplot as plt
from scipy.integrate import odeint

#solving our differential equation by creating an ode function that takes the initial conditions and uses the 
#inverse rotation matrix to compute dq/dt
def ode_func(qdot,t):
    qx=qdot[0]
    qy=qdot[1]
    qz=qdot[2]
    
    #given constant angular velocity D
    om=np.array([0.1, 0.2, 0.4]) #rad/s
    
    #simplified rotation matrix in terms of qx, qy, qz
    A=np.array([math.cos(qz)/math.cos(qy), -math.sin(qz)/math.cos(qy), 0
        , math.sin(qz), math.cos(qz), 0
        ,-math.tan(qy)*math.cos(qz), math.tan(qy)*math.sin(qz), 1])
    A=A.reshape(3,3)
    
    #solving for dq/dt by calculating the dot product  
    qdot=np.matmul(A,om)
    return qdot

#starting the timer
import timeit
import time
start_time=time.time()
if __name__ == "__main__":
    
    #given initial conditions for qx, qy, qz
    qo=([0, 0, 0])    
    
    #setting up our time vector for the odeint function
    to=0
    tf=15
    n=10001
    t=np.linspace(to,tf,n)
    
    #using the odeint function to integrate qdot over the specified time t
    #returns Euler angles in one output vector
    qdot=odeint(ode_func,qo,t)

#plotting the Euler angles over 15 seconds
plt.plot(t,qdot[:,0],label="qx")
plt.plot(t,qdot[:,1],label="qy")
plt.plot(t,qdot[:,2],label="qz")
plt.legend(loc="upper left")
plt.xlabel("Time (sec)")
plt.ylabel("Euler Angles: Body XYZ (rad)")
plt.title("Approximate Solution with ODE Integrator")
plt.show()

#time to execute the code
print("--- %s seconds ---" % (time.time() - start_time))