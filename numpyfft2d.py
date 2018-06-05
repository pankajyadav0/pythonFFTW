

execfile('/home/pankaj/pythonCodes/pyFFTW/arrayDef_numpyfft2d.py')

Lx = float(1.0)
Ly = float(1.0)

halfnx = nx/2
halfny = ny/2

dx = float(1.0) #(Lx/nx)
dy = float(1.0) #(Ly/ny)

px = float(2*pi/(nx*dx)) 
py = float(2*pi/(ny*dy))

dkx = 2.0 * pi/(nx*dx)
dky = 2.0 * pi/(ny*dy)

for i in range(nx):
    for j in range(ny):
        fun[i][j] = sin(i*px*dx) + cos(j*py*dy)

funfft = fft.fft2(fun)

for i in range(nx):
    for j in range(ny):
        if (i<halfnx):
            kx[i][j] = float(i * dkx)
        if (i>=halfnx):
            kx[i][j] = float(i - nx) * dkx
        if (j<halfny):
            ky[i][j] = float(j * dky)
        if (j>=halfny):
            ky[i][j] = float(j - ny)*dky
        dfunfft_x[i][j] = 1J * kx[i][j] * funfft[i][j]
        dfunfft_y[i][j] = 1J * ky[i][j] * funfft[i][j]

dfun_x = fft.ifft2(dfunfft_x)
dfun_y = fft.ifft2(dfunfft_y)

for i in range(nx):
    for j in range(ny):
        gradient[i][j] = sqrt(real(dfun_x[i][j])*real(dfun_x[i][j]) + real(dfun_y[i][j]) * real(dfun_y[i][j]) )

fp = open('Derivative2d_Data','w')
for i in range(nx):
    for j in range(ny):
        fp.write('{}\t{}\t{}\t{}\n'.format(i,j,fun[i][j], gradient[i][j]))
    fp.write('\n')
fp.close()

