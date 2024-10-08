#%%
"""
This script is used to  a two-lens optics with specific F/#.
One case is to used two single-curvedSurface lenses.
Another is to used two double-surface lenses.

The input parameters:
1. F/#.
2. Separated distance between two lenses: L.
3. refractive index of the lens material: n.
4. Aparture size: D.

Formula:
a. f_eff = F/# * D   effective focal length
   
   1/f_eff = 1/f1 + 1/f2 -1/f1f2

b. conic surface (ideally)
   
   r = (n-1)*f / (n*cos[theta] -1)

   r = [(e-1)(e+1)a]/[e cos[theta] -1]

   so,
   n = e
   f = a(1+e)
   R (1/curvature) = b^2/a = (c^2-a^2)/a

   k (conic constance) = -e^2

c. constraints: to keep telecentricity of the optics
   one rule is the f2 should be equal to the lens distance L.

   L = f2

"""
import numpy as np
import matplotlib.pyplot as plt
#%%
# hyperbole lens
def One_surface_hyperb(f,n):
    e = n
    a = f/(1+e)
    c = a*e
    k = -e**2
    R = (c**2-a**2)/a

    zemax_lens = {'k': k,
                  'R': R,
                  'f': f,
                  'n': n}
    return zemax_lens

def Dual_lens(f_eff, L):
    f2 = L
    
    
    