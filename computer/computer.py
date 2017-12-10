import os
import numpy as np

os.system('cls')

K = 200
X = np.random.randint(0, 101, size=(K, 5))
Objective = [0] * K
for k in range(K):
    while (X[k][0] - X[k][1] < 23) or (X[k][1] - 2 * X[k][2] < 25) or (X[k][2] + X[k][3] < 26) or (X[k][3] - X[k][4] < 12):
        X[k][0] = np.random.randint(0,101)
        X[k][1] = np.random.randint(0,101)
        X[k][2] = np.random.randint(0,101)
        X[k][3] = np.random.randint(0,101)
        X[k][4] = np.random.randint(0,101)

for k in range(K):
    Objective[k] = 3 * X[k][0] + 10 * X[k][1] + 5 * X[k][2] + 2 * X[k][3] - 3225 * X[k][4] - 3 * X[k][0] * X[k][2] - 4 * X[k][1] * X[k][2] + 6 * X[k][2] * X[k][4]

Point_k = 0
for k in range(1, K):
    if Objective[k] < Objective[Point_k]:
        Point_k = k

print('Incumbent solution:',end='\t')
print('x1=', X[Point_k][0],';\t x2=', X[Point_k][1],';\t x3=', X[Point_k][2],';\t x4=', X[Point_k][3],';\t x5=', X[Point_k][4],'\tObjective value=', Objective[Point_k])

for iteration in range(10000):
    for k in range(0, K):
        if k != Point_k:
            X[k][0] = np.random.randint(0, 101)
            X[k][1] = np.random.randint(0, 101)
            X[k][2] = np.random.randint(0, 101)
            X[k][3] = np.random.randint(0, 101)
            X[k][4] = np.random.randint(0, 101)
            while (X[k][0] - X[k][1] < 23) or (X[k][1] - 2 * X[k][2] < 25) or (X[k][2] + X[k][3] < 26) or (X[k][3] - X[k][4] < 12):
                X[k][0] = np.random.randint(0,101)
                X[k][1] = np.random.randint(0,101)
                X[k][2] = np.random.randint(0,101)
                X[k][3] = np.random.randint(0,101)
                X[k][4] = np.random.randint(0,101)
            Objective[k] = 3 * X[k][0] + 10 * X[k][1] + 5 * X[k][2] + 2 * X[k][3] - 3225 * X[k][4] - 3 * X[k][0] * X[k][2] - 4 * X[k][1] * X[k][2] + 6 * X[k][2] * X[k][4]
    for k in range(0, K):
        if Objective[k] < Objective[Point_k]:
            Point_k = k
    print('iteration:', iteration + 1,end='\t')
    print('x1=', X[Point_k][0],';\t x2=', X[Point_k][1],';\t x3=', X[Point_k][2],';\t x4=', X[Point_k][3],';\t x5=', X[Point_k][4],'\tObjective value=', Objective[Point_k])