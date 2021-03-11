import numpy as np
import sympy as sym
from sympy import *
from numpy import matrix
from numpy import linalg
from sympy import MatrixSymbol, Matrix
import math
from numpy.linalg import inv
from matplotlib import pyplot as plt

from rot_matrix import rot_matrix
from rot_matrixODE import rot_matrixODE

#Our first goal is to make a loop where q1, q2, and q3 will be changing with time. We want to plot Euler
#angles over the first 15 seconds with initial condition that qx=qy=qz=0.
#Using forward Euler method to estimate our curves

#starting the timer
import timeit
import time
start_time=time.time()

if __name__ == "__main__":
    #given initial conditions for qx, qy, qz
    qx_o=0
    qy_o=0
    qz_o=0
    
    #setting up our delta t and our t vector for integration
    to=0
    tf=15
    n=10001
    del_t=(tf-to)/(n-1)
    t=np.linspace(to,tf,n)
    
    #initializing the qx, qy, qz vectors
    qx=np.zeros([n])
    qy=np.zeros([n])
    qz=np.zeros([n])

    qx[0]=qx_o
    qy[0]=qy_o
    qz[0]=qz_o
    
    #given constant angular velocity D
    om=np.array([0.1, 0.2, 0.4]) #rad/sec
    om=om.reshape(3,1)
    
    #calling the functions to get our ODE matrix
    R1=rot_matrix(qx[0], qy[0], qz[0])
    w=rot_matrixODE(R1,qz[0])

#for loop that solves the ODEs by integrating dq/dt over the specified delta t
for i in range(1,n):
    #solving for dq/dt by calculating the dot product
    qdot=np.matmul(w.inv(),om)
    
    qx[i]=del_t*(qdot[0])+qx[i-1]
    qy[i]=del_t*(qdot[1])+qy[i-1]
    qz[i]=del_t*(qdot[2])+qz[i-1]
    
    R1=rot_matrix(qx[i], qy[i], qz[i])
    w=rot_matrixODE(R1,qz[i])

#plotting the Euler angles over 15 seconds
plt.plot(t,qx,label="qx")
plt.plot(t,qy,label="qy")
plt.plot(t,qz,label="qz")
plt.legend(loc="upper left")
plt.xlabel("Time (sec)")
plt.ylabel("Euler Angles: Body XYZ (rad)")
plt.title("Approximate Solution with Forward Euler's Method")
plt.show()

#time to execute the code
print("--- %s seconds ---" % (time.time() - start_time))