import numpy as np

A = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]])

G = np.zeros((A.shape[0], A.shape[0]))
N = np.zeros(A.shape[0])

for i in range(A.shape[0]):
    s = 0
    for j in range(A.shape[0]):
        s += A[i, j]
    N[i] = s

q = 0.15

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


eigenvector(A)
