import numpy as np

A = np.zeros((15, 15))
A[0][1] = 1
A[0][8] = 1
A[1][2] = 1
A[1][4] = 1
A[1][6] = 1
A[2][1] = 1
A[2][5] = 1
A[2][7] = 1
A[3][2] = 1
A[3][11] = 1
A[4][0] = 1
A[4][9] = 1
A[5][9] = 1
A[5][10] = 1
A[6][9] = 1
A[6][10] = 1
A[7][3] = 1
A[7][10] = 1
A[8][4] = 1
A[8][5] = 1
A[8][9] = 1
A[9][12] = 1
A[10][14] = 1
A[11][6] = 1
A[11][7] = 1
A[11][10] = 1
A[12][8] = 1
A[12][13] = 1
A[13][9] = 1
A[13][10] = 1
A[13][12] = 1
A[13][14] = 1
A[14][11] = 1
A[14][13] = 1

# A[0][9] = 1
# A[2][9] = 1
# A[14][9] = 1
# A[7][9] = 1

# A[7][10] = 3
# A[11][10] = 3

G = np.zeros((A.shape[0], A.shape[0]))
N = np.zeros(A.shape[0])

for i in range(A.shape[0]):
    s = 0
    for j in range(A.shape[0]):
        s += A[i, j]
    N[i] = s

q = 0.15
# q=0.02
# q=0.6

n = A.shape[0]
for i in range(A.shape[0]):
    for j in range(A.shape[0]):
        G[i, j] = (q / n) + ((A[j, i] * (1 - q)) / N[j])


def eigenvector(A):
    P = np.full(A.shape[0], 1)
    for b in range(20000):
        P = np.dot(G, P)

    s = 0
    for i in range(A.shape[0]):
        s += P[i]

    for i in range(A.shape[0]):
        P[i] /= s

    print(P)


print(A)
print(G)
eigenvector(A)
