import numpy as np
import matplotlib.pyplot as plt


# define function
def f(x):
    return a * (x**b)


# inputs

x = [4,2.25,1.45,1.0,0.65,0.25,0.006]
y = [0.398,0.298,0.238,0.198,0.158,0.098,0.048]


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

    xList = np.linspace(0, 4)
    yList = f(xList)

    plt.plot(xList, yList, color = 'green')
    plt.show()


n = len(x)
z = np.zeros(n)
t = np.zeros(n)

for i in range(n):
    t[i] = np.log(x[i])
    z[i] = np.log(y[i])

t_sum = 0
z_sum = 0
tz_sum = 0
tt_sum = 0
# print(n)

for i in range(n):
    t_sum = t_sum + t[i]
    z_sum = z_sum + z[i]
    tz_sum = tz_sum + t[i] * z[i]
    tt_sum = tt_sum + t[i] ** 2

print(x_sum)
print(y_sum)
print(xz_sum)
print(xx_sum)

a1 = (n * tz_sum - (t_sum * z_sum)) / (n * tt_sum - t_sum ** 2)
a0 = (z_sum / n) - a1 * (t_sum / n)

a = np.exp(a0)
b = a1

plot()

print("The exponential model of non linear regression fits the data best")
print("The value of a is : ", "%.4f" % a)
print("The value of b is : ", "%.4f" % b)
print("f(x) = %.4f * x ^ (%.4f)" % (a, b))

xP = .16
yP = f(xP)
yPp = round(yP, 2)
print("Relative risk of a person having 160 pound weight and %.2f BAC to crash if they drive after having a 6-pack "
      "of beer is : %.2f" % (xP, yPp))