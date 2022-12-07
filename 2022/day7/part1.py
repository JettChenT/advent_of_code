cnt = 0

class Item:
    def __init__(self, typ, parent, size=0) -> None:
        self.typ = typ
        self.parent=parent
        if typ==0: # file
            self.size = size 
            self.content = None
        else: # folder
            self.size=None
            self.content = {}
    
    def get_size(self):
        if self.typ==0:
            return self.size
        else:
            self.size = sum([i.get_size() for i in self.content.values()])
            if self.size<100_000:
                global cnt
                cnt+=self.size
            return self.size

root = Item(1,None)
cur = root
for l in open('test.txt').readlines():
    if l.startswith('$'):
        tail = l[2:]
        if tail.startswith("cd"):
            target = tail.split()[1]
            if target=='..':
                cur = cur.parent
            elif target=='/':
                cur = root
            else:
                cur = cur.content[target]
    else:
        a,b = l.split()
        if a=='dir':
            cur.content[b]=Item(1,cur)
        else:
            cur.content[b]=Item(0,cur,int(a))

root.get_size()
print(cnt)