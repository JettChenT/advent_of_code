import numpy as np
fname = 'sample.txt'
grid = []
for l in open(fname).readlines():
    grid.append([])
    for c in l.strip('\n'):
        grid[-1].append(int(c))
    
array = np.array(grid)
seen = np.zeros(array.shape, dtype=np.int32)
mtcnt = 0
for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        vecs = [(0,1), (0,-1), (1,0), (-1,0)]
        tcnt = 1
        for dir in vecs:
            x,y = i,j
            cnt = 1
            while True:
                x+=dir[0]
                y+=dir[1]
                if x<0 or y<0 or x>=array.shape[0] or y>=array.shape[1]:
                    cnt-=1
                    break
                if array[x,y]>=array[i,j]:
                    break
                cnt+=1
            tcnt *= cnt
        seen[i,j] = tcnt
        mtcnt = max(mtcnt, tcnt)

print(mtcnt)