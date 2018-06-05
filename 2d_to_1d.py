

nx = 3
ny = 4

g = []

for i in range(nx):
    g.append([])

for i in range(nx):
    for j in range(ny):
        g[i].append(j)
        g[i][j] = 0.0

for i in range(nx):
    for j in range(ny):
        g[i][j] = j + i*ny

#print ("Using range...")
for i in range(0,nx):
    output = ""                  #setting output to empty string
    for j in range(0,len(g[i])):
        output += str(g[i][j]) + "\t"
    
    print(output )

print ("\n")

#print("Using enhanced loop...")
for sara in g:
    output = ""
    for pank in sara:
        output += str(pank) + "\t"
    print (output)

print g[2][3]
print g[1][3]

g1d = []

for i in range(nx*ny):
    g1d.append([])

for i in range(nx):
    for j in range(ny):
        ii = j + i * ny
        g1d[ii] = g[i][j]

print g1d


'''
matrix = [[]]

for j in range(nx):
    matrix = [[j for i in xrange(2)] for i in xrange(5)]

from itertools import count, takewhile
matrix = [[i for i in takewhile(lambda j: j < (k+1) * 10, count(k*10))] for k in range(10)]

rows_count = 3
cols_count = 3

two_d_array = [[0 for j in range(cols_count)] for i in range(rows_count)]

for i in range(0,rows_count):
    for j in range(0,cols_count):
        two_d_array[i][j] = i+j

print two_d_array
'''


