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
   
   1/f_eff = 1/f1 + 1/f2 -L/f1f2

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
# 1. single surface lens
''' 
In the approprate paraxial limit, the hyperb and spheric
sag of the surface becomes

z ~ r^2/(2f[n-1])

'''
# hyperbole lens
def hyperbolic_plano_lens(f,n):
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
# spheric lens
def spherical_plano_lens(f,n):
    R = f*(n-1)
    zemax_lens = {'k': 0,
                  'R': R,
                  'f': f,
                  'n': n}
    return zemax_lens

# plano-curvedsurf lens
def plano_surf_lens(f,n,tc,
                    D_size=10,
                    poly_order = 10):
    """
    'tc' is the center thickness of the lens.
    """
    def sag(r):
        #r2 = x**2 + y**2
        r2 = r**2
        f2 = f**2
        b = f + (n-1)*tc - np.sqrt(f2 +r2)
        a = n*np.sqrt(1+r2/(n**2*(f2+r2)-r2)) -1
        return b/a
    rho = np.linspace(0,1,50)
    z   = sag(D_size/2*rho)
    coeffi = np.polyfit(rho**2, z, poly_order)

    zemax_lens = {'k': 'polynomial Surface',
                  'R': '',
                  'sag': sag,
                  'coeff': coeffi,
                  'Normalization': D_size/2,
                  'f': f,
                  'n': n}
    return zemax_lens

# Double surface lens
def Double_surf_lens(f,n):
    pass

# 2.  calculate the required focal length of the 
# two-lens system, with constraint of separation distance
# of the lenses is equial to f2

def Dual_lens(f_eff, L):
    f2 = L
    f1 = None
    return f1, f2

#%%    
index = 1.525#3.416 #
f = Dual_lens(640, 640)
lens1 = hyperbolic_plano_lens(2*f[1],index)
lens2 = hyperbolic_plano_lens(f[1],index)
print(lens1,'\n',lens2)
# %%
"""
lens3 = plano_surf_lens(f[0],index,1,D_size=400,poly_order = 20)
# %%
lens3
# %%
x = np.linspace(-1,1,101)
Sag = np.poly1d(lens3['coeff'])
y = Sag(x**2)

# %%
plt.figure(figsize=(5,3))
plt.plot(y,x*50)
plt.axis('equal')
plt.show()
# %%
"""
