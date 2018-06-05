
import fftw3
import pyfftw
from numpy import *

nx = int(64)
ny = int(64)

fun = []
gradient = []
kx = []
ky = []
dfunfft_x = []
dfunfft_y = []

for i in range(nx):
    fun.append([])
    kx.append([])
    ky.append([])
    gradient.append([])
    dfunfft_x.append([])
    dfunfft_y.append([])

for i in range(nx):
    for j in range(ny):
        fun[i].append(j)
        kx[i].append(j)
        ky[i].append(j)
        dfunfft_x[i].append(j)
        dfunfft_y[i].append(j)
        gradient[i].append(j)

