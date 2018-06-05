

import fftw3
import pyfftw
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

nx = int(64)
ny = int(64)
Lx = float(1.0)
Ly = float(1.0)

dx = float(1.0) #(Lx/nx)
dy = float(1.0) #(Ly/ny)

halfnx = int(nx/2)
halfny = int(ny/2)

dkx = float(2.0*np.pi/(nx*dx))
dky = float(2.0*np.pi/(ny*dy))

px = float(2*np.pi/(nx*dx)) 
py = float(2*np.pi/(ny*dy))

'''take = pyfftw.empty_aligned(nx*ny, dtype='complex128', n=16)
give = pyfftw.empty_aligned(nx*ny, dtype='complex128', n=16)

fft_object = pyfftw.FFTW(take, give, direction='FFTW_FORWARD')
ifft_object = pyfftw.FFTW(take, give, direction='FFTW_BACKWARD')
'''
take2d = pyfftw.empty_aligned((nx,ny), dtype='complex128', n=16)
give2d = pyfftw.empty_aligned((nx,ny), dtype='complex128', n=16)

fft_object = pyfftw.FFTW(take2d, give2d, direction='FFTW_FORWARD')
ifft_object = pyfftw.FFTW(take2d, give2d, direction='FFTW_BACKWARD')

fun1 = []
fun = []
funfft = []
dfunfft_x = []
dfunfft_y = []
dfun_x = []
dfun_y = []
gradient = []
c = []
kx = []
ky = []

for i in range(nx*ny):
    fun1.append([])
    funfft.append([])
    dfunfft_x.append([])
    dfunfft_y.append([])
    c.append([])
    gradient.append([])
    kx.append([])
    ky.append([])

for i in range(nx):
    for j in range(ny):
        fun1[j + i*ny] = np.sin(i*px*dx) + np.cos(j*py*dy)

for i in range(nx):
    fun.append([])

for i in range(nx):
    for j in range(ny):
        fun[i].append(j)

for i in range(nx):
    for j in range(ny):
        ii = j + i * ny
        fun[i][j] = fun1[ii]

#take2d[:] = fun
#give2d[:] = 0.0
#c[:] = take2d + 1J*give2d
funfft1 = fft_object(fun)

for i in range(nx):
    for j in range(ny):
        ii = j + i * ny
        funfft[ii] = funfft1[i][j]

for i in range(nx):
    for j in range(ny):
        if (i<halfnx):
            kx[j+i*ny] = float (i*dkx)
        if (i>=halfnx):
            kx[j+i*ny] = float (i - nx)*dkx
        if (j<halfny):
            ky[j+i*ny] = float (j*dky)
        if (j>=halfnx):
            ky[j+i*ny] = float (j - ny)*dky
        dfunfft_x[j + i *ny] = 1J * kx[j+i*ny] * funfft[j + i * ny]
        dfunfft_y[j + i *ny] = 1J * ky[j+i*ny] * funfft[j + i * ny]

fp = open('Derivative2d_Data','w')
for i in range(nx):
    for j in range(ny):
        fp.write('{}\t{}\t{}\t\t{}\n'.format(i,j,fun1[j+i*ny], np.real(funfft[j+i*ny])))
    fp.write('\n')
fp.close()


take[:] = dfunfft_x
give[:] = 0.0
c[:] = take + 1J*give
dfun_x = ifft_object()
#print dfun_x

#plt.plot(ky)
#plt.plot(dfun_x)
#plt.show()

take[:] = dfunfft_y
give[:] = 0.0
c[:] = take + 1J*give
dfun_y = ifft_object()

for i in range(nx):
    for j in range(ny):
        gradient[j + i *ny] = np.sqrt(np.real(dfun_x[j+i*ny])*np.real(dfun_x[j+i*ny])  + np.real(dfun_y[j+i*ny])*np.real(dfun_y[j+i*ny]) )

fp = open('Derivative2d_Data','w')
for i in range(nx):
    for j in range(ny):
        fp.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(i,j,fun[j+i*ny], np.real(funfft[j+i*ny]), np.real(dfun_x[j+i*ny]), np.real(dfun_y[j+i*ny]), np.real(gradient[j+i*ny])))
    fp.write('\n')
fp.close()


'''
fun = []
funfft = []
dfunfft_x = []
dfunfft_y = []
dfun_x = []
dfun_y = []
gradient = []
grad = []
c = []
kx = []
ky = []

for i in range(nx):
    fun.append([])
    dfunfft_x.append([])
    dfunfft_y.append([])
    c.append([])
    gradient.append([])
    kx.append([])
    ky.append([])

for i in range(nx*ny):
    grad.append([])

for i in range(nx):
    for j in range(ny):
        fun[i].append(j)
        fun[i][j] = 0.0
        dfunfft_x[i].append(j)
        dfunfft_x[i][j] = 0.0
        dfunfft_y[i].append(j)
        dfunfft_x[i][j] = 0.0
        c[i].append(j)
        c[i][j] = 0.0
        gradient[i].append(j)
        gradient[i][j] = 0.0
        kx[i].append(j)
        kx[i][j] = 0.0
        ky[i].append(j)
        ky[i][j] = 0.0

for i in range(nx):
    for j in range(ny):
        fun[i][j] = np.sin(i*px*dx) + np.cos(j*py*dy)

take2d[:] = fun
give2d[:] = 0.0
c[:] = take2d + 1J*give2d
funfft = fft_object()

for i in range(nx):
    for j in range(ny):
        if (i<halfnx):
            kx[i][j] = float (i*dkx)
        if (i>=halfnx):
            kx[i][j] = float (i - nx)*dkx
        if (j<halfny):
            ky[i][j] = float (j*dky)
        if (j>=halfnx):
            ky[i][j] = float (j - ny)*dky
        dfunfft_x[i][j] = 1J * kx[i][j] * funfft[i][j]
        dfunfft_y[i][j] = 1J * ky[i][j] * funfft[i][j]

take[:] = dfunfft_x
give[:] = 0.0
c[:] = take + 1J*give
dfun_x = ifft_object()
#print dfun_x

#plt.plot(ky)
#plt.plot(dfun_x)
#plt.show()

take[:] = dfunfft_y
give[:] = 0.0
c[:] = take + 1J*give
dfun_y = ifft_object()

for i in range(nx):
    for j in range(ny):
        gradient[i][j] = np.sqrt(np.real(dfun_x[i][j])*np.real(dfun_x[i][j])  + np.real(dfun_y[i][j])*np.real(dfun_y[i][j]) )

for i in range(nx):
    for j in range(ny):
        ii = j + i * ny
        grad[ii] = gradient[i][j]

fp = open('Derivative2d_Data','w')
for i in range(nx):
    for j in range(ny):
        fp.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(i,j,fun[i][j], np.real(funfft[i][j]), np.real(dfun_x[i][j]), np.real(dfun_y[i][j]), np.real(grad[j+i*ny])))
    fp.write('\n')
fp.close()
'''
