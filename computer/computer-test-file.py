import os
import numpy as np

os.system('cls')

K = 200
X = np.random.randint(0, 51, size=(K, 4))
Objective = [0] * K
for k in range(K):
    while (X[k][0] + X[k][1] +X[k][2] + X[k][3] != 25) or (5*X[k][0] + 2 * X[k][1] + 1* X[k][2] + 6*X[k][3] < 10):
        X[k][0] = np.random.randint(0,51)
        X[k][1] = np.random.randint(0,51)
        X[k][2] = np.random.randint(0,51)
        X[k][3] = np.random.randint(0,51)

for k in range(K):
    Objective[k] = 3 * X[k][0] + 12 * X[k][1] + 9 * X[k][2] + 5 * X[k][3] + 3 * X[k][0] * X[k][1] - 10 * X[k][0] * X[k][2] + 6 * X[k][0] * X[k][3] + X[k][1] * X[k][2]- 5 * X[k][1] * X[k][3] - 2 * X[k][2] * X[k][3]

Point_k = 0
for k in range(1, K):
    if Objective[k] < Objective[Point_k]:
        Point_k = k

print('Incumbent solution:',end='\t')
print('x1=', X[Point_k][0],';\t x2=', X[Point_k][1],';\t x3=', X[Point_k][2],';\t x4=', X[Point_k][3],'\tObjective value=', Objective[Point_k])


for iteration in range(10):
    for k in range(0, K):
        if k != Point_k:
            X[k][0] = np.random.randint(0,51)
            X[k][1] = np.random.randint(0,51)
            X[k][2] = np.random.randint(0,51)
            X[k][3] = np.random.randint(0,51)
            while (X[k][0] + X[k][1] +X[k][2] + X[k][3] != 25) or (5*X[k][0] + 2 * X[k][1] + 1* X[k][2] + 6*X[k][3] < 10):
                X[k][0] = np.random.randint(0,51)
                X[k][1] = np.random.randint(0,51)
                X[k][2] = np.random.randint(0,51)
                X[k][3] = np.random.randint(0,51)
            Objective[k] = 3 * X[k][0] + 12 * X[k][1] + 9 * X[k][2] + 5 * X[k][3] + 3 * X[k][0] * X[k][1] - 10 * X[k][0] * X[k][2] + 6 * X[k][0] * X[k][3] + X[k][1] * X[k][2]- 5 * X[k][1] * X[k][3] - 2 * X[k][2] * X[k][3]
    for k in range(0, K):
        if Objective[k] < Objective[Point_k]:
            Point_k = k
    print('iteration:', iteration + 1,end='\t')
    print('x1=', X[Point_k][0],';\t x2=', X[Point_k][1],';\t x3=', X[Point_k][2],';\t x4=', X[Point_k][3],'\tObjective value=', Objective[Point_k])
