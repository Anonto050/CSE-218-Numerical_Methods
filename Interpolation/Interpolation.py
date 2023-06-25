import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math

y=np.array([[0 for i in range(6)]
        for j in range(6)],dtype=float)

n = int(input('Enter number of data points: '))

# Making numpy array of n & n x n size and initializing
# to zero for storing x and y value along with differences of y
a = np.zeros((n))
b = np.zeros((n))

# Reading data points
print('Enter data for x and y: ')
for i in range(n):
    a[i] = float(input('x[' + str(i) + ']='))
    b[i] = float(input('y[' + str(i) + ']='))


def take_input():
    '''file=open("dissolveO2.csv")
    f=0
    for line in file:
        data=line.split(",")
        if f>0 :
            a.append(int(data[0]))
            b.append(float(data[1]))
            c.append(float(data[2]))
        f=f+1
    file.close()'''


def plot_graph(p,q,r,inp,quartic1,quartic2):
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    p.append(inp)
    q.append(quartic1)
    r.append(quartic2)
    final=dict()
    final2=dict()

    for i in range(len(p)):
        final[p[i]]=q[i]
        final2[p[i]]=r[i]
    p=sorted(p)
    for i in range(len(p)):
        q[i]=final[p[i]]
        r[i]=final2[p[i]]

    plt.plot(p,q,r,color='g',marker='o')
    plt.show()

def product(i, value, x):
    pro = 1
    for j in range(i):
        pro = pro * (value - x[j])
    return pro

def dividedDifference(x, y, n):
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                       (x[j] - x[i + j]))
    #print(y)
    return y


def applyFormula(value, x, y, n):
    sum = y[0][0]

    for i in range(1, n):
        sum = sum + (product(i, value, x) * y[0][i])

    return sum

#main function

inp=input("Enter the value of Temperature : ")
inp=int(inp)
temp={}


for i in range(n):
    y[i][0] = b[i]


y=dividedDifference(a, y, n)
quartic1=applyFormula(inp, a, y, n)

for i in range(n):
    for j in range(n):
        print(round(y[i][j],6),end = "  ")
    print()

print("\nValue at", inp, "is",
        round(applyFormula(inp, a, y, n), 2))

'''for i in range(4):
    x.append(d[i])
x=sorted(x)
for i in range(4):
    for j in range(len(a)):
        if(a[j]==x[i]):
            y[i][0] = b[j]
            break
n=4
y=dividedDifference(x, y, n)
cubic=applyFormula(inp, x, y, n)
error=math.fabs((quartic1-cubic)/quartic1)*100
print("\nAbsolute relative Approximate error: ",error)

n=5
x.clear()
for i in range(5):
    x.append(d[i])
x=sorted(x)

for i in range(5):
    for j in range(len(a)):
        if(a[j]==x[i]):
            z[i][0] = c[j]
            break

z=dividedDifference(x, z, n)
quartic2=applyFormula(inp, x, z, n)
print("\nValue at", inp, "is",
        round(applyFormula(inp, x, z, n), 2))

x.clear()
for i in range(4):
    x.append(d[i])
x=sorted(x)
for i in range(4):
    for j in range(len(a)):
        if(a[j]==x[i]):
            z[i][0] = c[j]
            break
n=4
z=dividedDifference(x, z, n)
cubic2=applyFormula(inp, x, z, n)
error=math.fabs((quartic2-cubic2)/quartic2)*100
print("\nAbsolute relative Approximate error: ",error)

plot_graph(a,b,c,inp,quartic1,quartic2)'''


