from numpy import *
from scipy.optimize import *
from math import sqrt

#inputs:
T = float(input("T (K)= "))
Fd = float(input("Fd (W/m^2)= "))
Fi = float(input("Fi (W/m^2)= "))
#Fi = (Fd*T) - 5.2
g = 5.67 * (10**(-8))
print("g=" + str(g))
h = float(input("h = "))


#systeme d'equation non lineaires
def syst(z):
    P = z[0]
    Ts = z[1]
    Tp = z[2]
    Fs = z[3]
    Fp = z[4]
    F = empty((5))
    F[0] = h*(Ts-T) + h*(Tp-T) - P
    F[1] = Fp + P - Fd - Fi
    F[2] = h*(Ts-T) + Fs - Fd - Fp
    F[3] = g*(Tp**4) - Fp
    F[4] = g*(Ts**4) - Fs
    return F
zGuess = array([1,1,1,1,1])
z = fsolve(syst,zGuess)
print(z)
