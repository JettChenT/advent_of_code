import numpy as np
fname = 'sample.txt'
grid = []
for l in open(fname).readlines():
    grid.append([])
    for c in l.strip('\n'):
        grid[-1].append(int(c))
    
array = np.array(grid)
seen = np.zeros(array.shape, dtype=np.int32)
for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        checks = [array[:i,j], array[i+1:,j], array[i,:j], array[i,j+1:]]
        mxes = []
        for a in checks:
            if len(a):
                mxes.append(a.max())
            else:
                mxes.append(-1)
        if min(mxes)<array[i,j]:
            seen[i,j]=1

# print(seen)
print(seen.sum())