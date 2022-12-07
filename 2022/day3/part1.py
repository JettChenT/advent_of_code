lines = open("input.txt").readlines()
cnt=0
for l in lines:
    a,b = l[:len(l)//2],l[len(l)//2:]
    # get intersection between sets of a and b
    sa,sb=set(a),set(b)
    intersection = sa.intersection(sb)
    for k in intersection:
        cnt += ord(k)- ((ord('A')-27) if k.isupper() else ord('a')-1)

print(cnt)