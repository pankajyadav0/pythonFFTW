
import pyfftw
import numpy as np
import matplotlib.pyplot as plt

nx=int(64)

a = pyfftw.empty_aligned(nx, dtype='complex128', n=16)
b = pyfftw.empty_aligned(nx, dtype='complex128', n=16)

fft_object = pyfftw.FFTW(a,b)
ifft_object = pyfftw.FFTW(a,b, direction='FFTW_BACKWARD')

L=float(13)
dx=float(L/nx)
px = float(4*np.pi/(nx*dx))
halfnx = int(nx/2)
dkx = float(2.0*np.pi/(nx*dx))

fun = []
c = []
kx = []
dfunfft = []

for i in range(nx):
    fun.append([])
    c.append([])
    kx.append([])
    dfunfft.append([])

for i in range(nx):
    fun[i] = np.sin(i*px*dx)

a[:] = fun
b[:] = 0.0
c[:] = a + 1J*b
funfft = fft_object()

#print fft_a
#print b


for i in range(0,nx):
    if i < halfnx:
        kx[i] = i * dkx
    if i == halfnx:
        kx[i] = 0.0
    if i > halfnx:
        kx[i] = (i - nx) * dkx
    dfunfft[i] = 1J * kx[i] * funfft[i]

a[:] = dfunfft
b[:] = 0.0
c[:] = a + 1J*b
dfun = ifft_object()
print dfun

plt.clf()
plt.plot(np.real(dfun))
plt.plot(fun)
plt.show()

np.allclose(a,b)
