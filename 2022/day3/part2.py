lines = open("input.txt").readlines()
cnt=0
for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')
for i in range(0,len(lines),3):
    # print(i)
    sa,sb,sc=set(lines[i]),set(lines[i+1]),set(lines[i+2])
    intersection = sa.intersection(sb).intersection(sc)
    for k in intersection:
        print(ord(k))
        cnt += ord(k)- ((ord('A')-27) if k.isupper() else ord('a')-1)

print(cnt)