mx = -1
with open('./input.txt') as f:
    lines = f.readlines()

cur = 0
for l in lines:
    tmp = l.strip('\n')
    if tmp=="":
        mx=max(cur,mx)
        cur=0
        continue
    cur+=int(tmp)

print(mx)
