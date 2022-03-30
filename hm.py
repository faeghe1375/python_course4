import math as mt
import numpy as np
def sin(d:float, N:int=10):
    s = 0
    x=d * mt.pi / 180
    for n in range(N):
        s += (-1)**n * x**(2*n + 1) / mt.factorial(2*n + 1)
    return s
        
    
