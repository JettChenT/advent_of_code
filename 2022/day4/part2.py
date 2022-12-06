lines = open('./input.txt').readlines()
cnt=0
def toint(x):
    return (int(x[0]),int(x[1]))
for l in lines:
    ra,rb = l.split(',')
    a =toint(ra.split('-'))
    b =toint(rb.split('-'))
    tmp = sorted([a,b])
    if tmp[0][1]>=tmp[1][0] or tmp[0][0]==tmp[1][0]:
        cnt+=1

print(cnt)