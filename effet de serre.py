from numpy import *
from scipy.optimize import *


#inputs:
T = float(input("T = "))
Fd = float(input("Fd = "))
Fi = float(input("Fi = "))
g = 5.67 * (10**(-8))
h = 4
def syst(z):
    P = z[0]
    Ts = z[1]
    Tp = z[2]
    Fp = z[3]
    Fs = z[4]
    F = empty((5))
    F[0] = h*(Ts-T) + h*(Tp-T) - P
    F[1] = Fp + P - Fd - Fi
    F[2] = h*(Ts-T) + Fs - Fd - Fp
    F[3] = g*(Tp**4) - Fp
    F[4] = g*(Ts**4) - Fs
    return F
xGuess = array([1,1,1,1,1])
z = fsolve(syst,xGuess)
print(z)
