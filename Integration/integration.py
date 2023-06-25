import numpy as np
from matplotlib import pyplot as plt


def f(x):
    denominator = 300*x
    numerator = 1+np.exp(x)

    #return denominator / numerator
    return 2000*np.log(140000/(140000-2100*x))-9.8*x

float_formatter = "{:.4}".format

def error(prev,new) :
    return (abs(new-prev)/new)*100


def trapezoidal(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)

    y = [f(i) for i in x]

    print("\nTrapezoidal Rule : \n")

    print('Value of h : %.4f'%h)

    print(x)
    print(y)

    integration = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])

    print('I : %.4f'%integration)

    return integration


def simpsons(a, b, n):

    h = (b-a)/(n)
    x = np.linspace(a, b, n + 1)
    y = [f(i) for i in x]

    print("\nSimpson's 1/3 Rule : \n")

    print('Value of h : %.4f' % h)

    print(x)
    print(y)

    integration = 0
    for i in range(2,n+1,2) :
        integration = integration + (h / 3) * (y[i-2] + 4 * f((x[i]+x[i-2])/2) + y[i])
    #j = (h / 3) * (y[0] + 2 * sum(y[2:2*n - 1:2]) + 4 * sum(y[1:2*n:2]) + y[2*n])

    print('I : %.4f' % integration)

    return integration

def plot():


    lst = [1.22*10**-4, 1.20*10**-4, 1.0*10**-4, 0.8*10**-4, 0.6*10**-4, 0.4*10**-4, 0.2*10**-4]
    x = np.array(lst)
    lst2 = []
    for i in lst:
        lst2.append(simpsons(1.22 * 10 ** -4,i,5))
    y = np.array(lst2)

    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.grid(color = 'blue',linestyle = '--',linewidth = 0.5)

    plt.xlabel("Oxygen Concentration")
    plt.ylabel("Time in Seconds")
    plt.plot(x,y,marker = 'o')
    '''for i in range(6):
        xs = [x[i], x[i], x[i + 1], x[i + 1]]
        ys = [0, y[i], y[i + 1], 0]
        plt.fill(xs, ys, 'b', edgecolor='b', alpha=0.2)'''
    plt.title("Simpson's 1/3 Rule, N = 10")
    plt.show()

'''main : '''


n = int(input("Enter value of N : \n"))

a = 8
b = 30
new = 0

ans1 = trapezoidal(a,b,n)
ans2 = simpsons(a,b,n)

'''for i in range(1, 6):
    prev = new
    new = trapezoidal(a, b, i)

    if i>1 :
        err = error(prev,new)
    if i==1 :
        print("\nTrapezoidal Rule : \n")
        print("Value of n  "+"   Approximate Value "+"   Absolute Approximate Relative Errors")
        print(f"     {i}           {round(new, 4)}            ---------")
    else :
        print(f"     {i}           {round(new, 4)}            {float_formatter(err)} %")

for i in range(1, 6):
    prev = new
    new = simpsons(a, b, i)
    if i > 1:
        err = error(prev, new)

    if i==1 :
        print("\nSimpson's 1/3 Rule : \n")
        print("Value of n  "+"   Approximate Value "+"   Absolute Approximate Relative Errors")
        print(f"     {i}           {round(new, 4)}            ---------")
    else:
        print(f"     {i}           {round(new, 4)}            {float_formatter(err)} %")'''

#plot()