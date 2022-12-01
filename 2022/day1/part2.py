with open('./input.txt') as f:
    lines = f.readlines()

lst = []
cur = 0
for l in lines:
    tmp = l.strip('\n')
    if tmp=="":
        lst.append(cur)
        cur=0
        continue
    cur+=int(tmp)

print(sum(sorted(lst)[-3:]))
