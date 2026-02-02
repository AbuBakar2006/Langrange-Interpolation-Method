import numpy as np 

x = [0.8, 1] 
y = [0.22363362, 0.65809197] 

n = len(x) 
X = float(input('Enter X: ')) 
S = 0 

L = np.zeros((n, 1)) 

for i in range(n): 
  L[i] = 1 

for j in range(n): 
  if j != i: 
  L[i] *= (X - x[j]) / (x[i] - x[j]) 
  S += y[i] * L[i] 

print('For x = %.1f, y = %.10f' % (X, S)) 
