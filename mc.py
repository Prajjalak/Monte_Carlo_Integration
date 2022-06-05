# Author: Prajjalak Chattopadhyay
# Monte-Carlo Integration
# Not using any integration library

import numpy as npy
import matplotlib.pyplot as mplt
from scipy import random
from tqdm import tqdm
import random
from multiprocessing import Pool, freeze_support
from itertools import repeat


# Values
a=0                 # Lower limit of integral
b=(npy.pi/2)        # Upper lilit of integral
start=0             # Iteration start value
incr=1000           # Iteration increment value
maxiter=1E+5        # Iteration max value

# Internal variables
I=[]
N=[]
err=[]
V=(npy.pi)**3/8


def f(x,y,z):        # Define your function here
    return npy.exp(-10*(x-1)**2)/((npy.sin(x))**2+(npy.sin(y))**2+(npy.sin(z))**2)

def Integral(i,n):        # Integration function for multiprocessing routine
    return V/n*f(arrayx[i],arrayy[i],arrayz[i])


for n in tqdm(range(int(start),int(maxiter),int(incr)),desc="Status",ascii=False,ncols=100):

    # Array of length N filled with zeros 
    arrayx = npy.zeros(n)
    arrayy = npy.zeros(n)
    arrayz = npy.zeros(n)
    
    for i in range (len(arrayx)):
        arrayx[i] = random.uniform(a,b) 
        arrayy[i] = random.uniform(a,b)
        arrayz[i] = random.uniform(a,b)
        
    if __name__=="__main__":
        freeze_support()
        i_list = npy.arange(n)
        W_pool = Pool()
        data = W_pool.starmap(Integral, zip(i_list, repeat(n)))
        W = 0
        W = sum(data)
        
        I.append(W)
        if len(I)>1:
            N.append(n)
            err.append(npy.std(I))
        
    
print ('Integration value:',W)


mplt.figure(1)
mplt.plot(N,err,'r')
mplt.plot(N,err,'b*')
mplt.title('Monte Carlo Integration - Error')
mplt.xlabel('N')
mplt.ylabel('Standard Deviation Error')
mplt.xlim(0,int(maxiter))
mplt.ylim(0,0.5)
mplt.grid(True)
mplt.show()
