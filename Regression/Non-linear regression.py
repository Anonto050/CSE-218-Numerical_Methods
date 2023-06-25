import numpy as np
import matplotlib.pyplot as plt

# define function
def f(x):
    return a0 + a1 * x + a2 * x**2 + a3 * x**3


# inputs
x = [0,10,20,30,40,50,60,70,80,90,100]
y = [10.3,13.5,13.9,14.2,11.6,10.3,9.7,9.6,14.1,19.8,31.1]


# plot graph to guess the solution
def plot():

    xG = np.array(x,dtype = float)
    yG = np.array(y,dtype = float)

    plt.xlabel("Years")
    plt.ylabel("Immigration Population (in millions)")

    for j in range(len(xG)):
        plt.plot(xG[j], yG[j], color = 'green',marker='o',)

    font2 = {'family': 'Times New Roman', 'color': 'blue', 'size': '18'}

    plt.grid(color = 'blue',linestyle = '--',linewidth = 0.5)
    plt.title("Curve Fitting", fontdict=font2)

    xList = np.linspace(0, 100)
    yList = f(xList)

    plt.plot(xList, yList, color = 'green')
    plt.show()

def GaussianElimination(A, B, pivot):
    n = B.size
    for i in range(0, n - 1):

        if pivot is True:
            max = np.abs(A[i, i])
            temp = i
            for k in range(i + 1, n):
                if np.abs(A[k, i]) > max:
                    max = np.abs(A[k, i])
                    temp = k

            A[[i, temp]] = A[[temp, i]]
            B[[i, temp]] = B[[temp, i]]

        for j in range(i + 1, n):
            coeff = A[j, i] / A[i, i]
            A[j, :] = A[j, :] - coeff * A[i, :]
            B[j] = B[j] - coeff * B[i]

    roots_matrix = np.zeros(n)
    roots_matrix[n - 1] = B[n - 1] / A[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum = sum + A[i, j] * roots_matrix[j]
        roots_matrix[i] = (B[i] - sum) / A[i, i]

    return roots_matrix

x_sum, x2_sum, x3_sum, x4_sum,x5_sum,x6_sum, y_sum, xy_sum, x2y_sum,x3y_sum = 0, 0, 0, 0, 0, 0, 0,0,0,0
n = len(x)

for i in range(n):
    x_sum += x[i]
    x2_sum += x[i]**2
    x3_sum += x[i]**3
    x4_sum += x[i]**4
    x5_sum += x[i]**5
    x6_sum += x[i]**6
    y_sum += y[i]
    xy_sum += x[i] * y[i]
    x2y_sum += (x[i]**2) * y[i]
    x3y_sum += (x[i]**3)*y[i]


list1 = [n, x_sum, x2_sum,x3_sum, x_sum, x2_sum,x3_sum,x4_sum, x2_sum, x3_sum, x4_sum,x5_sum,x3_sum, x4_sum,x5_sum,x6_sum]
A = np.array(list1, dtype='float64').reshape(4, 4)
B = np.array([y_sum, xy_sum, x2y_sum,x3y_sum])


print("The best-fit model for the foreign-born immigrants in the United States is Polynomial of 3rd Order")
result = GaussianElimination(A, B, True)
for i in range(result.size):
    print("The value of a0 is : ", "%.4f" % result[i])


a0 = result[0]
a1 = result[1]
a2 = result[2]
a3 = result[3]

print("f(x) = %.4f + (%.4f * x)+(%.4f * x**2)+(%.4f * x**3)" % (a0, a1,a2,a3))


xP = 110
yP = f(xP)
yPp = round(yP, 4)
print("The number of foreign-born immigrants in 2010 : %.4f million" % yPp)

plot()


