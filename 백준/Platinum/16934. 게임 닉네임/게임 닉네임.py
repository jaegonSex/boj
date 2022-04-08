class Trie():

    def __init__(self):
        self.trie={}

    def insert(self, word):
        t=self.trie
        for c in word:
            if c not in t:
                t[c]={}
            t=t[c]
        t['*']=True

    def startsWith(self, prefix):
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True
member={}
trie=Trie()
n=int(input())
for i in range(n):
    m=input()
    keys=member.keys()

    if m in keys:
        member[m]+=1
    else:
        member[m]=1

    prefix=False
    for j in range(1,len(m)):
        if trie.startsWith(m[:j]):
            continue
        else:

            prefix=m[:j]
            break

    if prefix:
        print(prefix)
    else:
        if member[m]==1:
            print(m)
        else:
            print(m,member[m],sep='')
    trie.insert(m)
