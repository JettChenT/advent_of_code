with open('./input.txt') as f:
    line = f.read()
N=14
for i in range(N,len(line)):
    tmp = line[i-N:i]
    if len(set(tmp))==N:
        print(i)
        break