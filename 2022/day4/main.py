lines = open('./input.txt').readlines()
cnt=0
def toint(x):
    return (int(x[0]),int(x[1]))
for l in lines:
    tmp = sorted([toint(k.split('-')) for k in l.split[',']])
    if tmp[0][1]>=tmp[1][1] or tmp[0][0]==tmp[1][0]:
        cnt+=1
print(cnt)