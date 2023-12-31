import numpy as np
import matplotlib.pyplot as plt


# define function
def f(x):
    return a * np.exp(b * x)


# inputs

x = [4,5,7,8,9,10]
y = [5800,5700,4200,4100,3100,2500]


# plot graph to guess the solution
def plot():

    xG = np.array(x,dtype = float)
    yG = np.array(y,dtype = float)

    plt.xlabel("Blood Alcohol Level")
    plt.ylabel("Relative Risk of Crushing")

    for j in range(len(xG)):
        plt.plot(xG[j], yG[j], color = 'green',marker='o',)

    font2 = {'family': 'Times New Roman', 'color': 'blue', 'size': '18'}

    plt.axhline(y=0)
    plt.axvline(x=0)
    plt.grid(color = 'blue',linestyle = '--',linewidth = 0.5)
    plt.title("Curve Fitting", fontdict=font2)

    xList = np.linspace(0, .22)
    yList = f(xList)

    plt.plot(xList, yList, color = 'green')
    plt.show()


n = len(x)
z = np.zeros(n)
for i in range(n):
    z[i] = np.log(y[i])

x_sum = 0
z_sum = 0
xz_sum = 0
xx_sum = 0
# print(n)

for i in range(n):
    x_sum = x_sum + x[i]
    z_sum = z_sum + z[i]
    xz_sum = xz_sum + x[i] * z[i]
    xx_sum = xx_sum + x[i] ** 2

print(x_sum)
print(z_sum)
print(xz_sum)
print(xx_sum)

a1 = (n * xz_sum - (x_sum * z_sum)) / (n * xx_sum - x_sum ** 2)
a0 = (z_sum / n) - a1 * (x_sum / n)

a = np.exp(a0)
b = a1

plot()

print("The exponential model of non linear regression fits the data best")
print("The value of a is : ", "%.4f" % a)
print("The value of b is : ", "%.4f" % b)
print("f(x) = %.4f * e ^ (%.4f * x)" % (a, b))

xP = .16
yP = f(xP)
yPp = round(yP, 2)
print("Relative risk of a person having 160 pound weight and %.2f BAC to crash if they drive after having a 6-pack "
      "of beer is : %.2f" % (xP, yPp))
