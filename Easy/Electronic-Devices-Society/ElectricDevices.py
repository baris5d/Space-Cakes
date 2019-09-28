first_line = input().split()

N = int(first_line[0]) 
M = int(first_line[1])
K = int(first_line[2])


values = input().split()

n=[]

for s in values: 
    n.append(int(s))

s = sorted(n)
previous = -1
idx = 0
for e in s:
    if previous != e:
        idx+=1
    previous = e
    
    if idx == K:
        print(e)
        break