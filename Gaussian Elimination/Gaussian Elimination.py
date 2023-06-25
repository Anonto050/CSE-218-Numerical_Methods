import numpy as np

float_formatter = "{:.4f}".format

def printAll(A) :
    for i in range(0,n):
        for j in range(0,n):
            if j==n-1 :
                print(float_formatter(A[i, j]))
            else :
                print(float_formatter(A[i,j]),end=" ")

def GaussianElimination(A, B, pivot, showall):
    n = B.size
    for i in range(0, n - 1):

        if pivot is True:
            max = np.abs(A[i, i])
            p = i
            for k in range(i + 1, n):
                if np.abs(A[k, i]) > max:
                    max = np.abs(A[k, i])
                    p = k

            A[[i, p]] = A[[p, i]]
            B[[i, p]] = B[[p, i]]

        c=1;
        for j in range(i + 1, n):
            m = A[j, i] / A[i, i]
            A[j, :] = A[j, :] - m * A[i, :]
            B[j] = B[j] - m * B[i]
            if showall is True :
                np.set_printoptions(formatter={'float_kind':float_formatter})
                print(f'Step : {i+1}')
                print(f'Sub-step : {c}')
                print("A : ")
                printAll(A)
                print("B : ")
                for k in range(0, n):
                    print(float_formatter(B[k]))
                print("\n")
            c=c+1
    x = np.zeros(n)
    x[n - 1] = B[n - 1] / A[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum = sum + A[i, j] * x[j]
        x[i] = (B[i] - sum) / A[i, i]

    return x


'''main : '''

n = int(input("Enter number of input variables : "))
lst = []

for i in range(0, n ):
    a = input()
    m = a.split()
    for k in range(0,n):
        lst.append(float(m[k]))

A = np.array(lst).reshape(n, n)

lst2 = []
for i in range(0, n):
    b = input()
    lst2.append(float(b))

B = np.array(lst2)

x = GaussianElimination(A, B, True, True)

print("Solution vector : ")
for i in range(0,n):
    print(float_formatter(x[i]))
