import numpy as np
import matplotlib.pyplot as plt
import math

def fx(x):
    return x*x - math.sin(x) - 0.5


x_values = np.linspace(-0.1, 0.2, num = 500)
tempY = []
for i in range (len(x_values)):
    tempY.append(fx(x_values[i]))
y_values = np.array(tempY)

plt.plot(x_values, y_values)
plt.axvline()
plt.axhline()
plt.grid()
plt.title("A graph to better understand Bisection Method")
plt.xlabel("x values (from -0.1 to 0.2)")
plt.ylabel("y values")
plt.show()

def bisection(xL, xU, eps, maxIteration):
    xM_prev = (xL + xU)/2
    xM_new = 0.0
    if fx(xL)*fx(xU) > 0:
        return
    for i in range (1, maxIteration):
        if fx(xL)*fx(xM_prev) < 0:
            xU = xM_prev
        elif fx(xL)*fx(xM_prev) > 0:
            xL = xM_prev
        xM_new = (xL + xU)/2
        error = abs((xM_new - xM_prev)/xM_new) * 100
        if error < eps:
            return xM_new
        else:
            xM_prev = xM_new
    return xM_new


def bisectionErrorPrint(xL, xU):
    xM_prev = (xL + xU) / 2
    xM_new = 0.0
    if fx(xL) * fx(xU) > 0:
        return
    print('Iteration no.       Absolute relative approx. error')
    print(1)
    for i in range(1, 21):
        if fx(xL) * fx(xM_prev) < 0:
            xU = xM_prev
            print(xM_prev)
        elif fx(xL) * fx(xM_prev) > 0:
            xL = xM_prev
            print(xM_prev)
        xM_new = (xL + xU) / 2
        error = abs((xM_new - xM_prev) / xM_new) * 100
        xM_prev = xM_new

        if i>1:
            if i < 10:
                print(str(i) + '\t\t\t\t\t'+ str(error))
            else:
                print(str(i) + '\t\t\t\t\t' + str(error))
    return xM_new


#root = bisection(0, 0.1, 0.5, 20)
root = bisectionErrorPrint(-1, 0)
print (root)
