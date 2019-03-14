"""
Created by Bhasfe
v0.1
"""

import copy

N = int(input())
V = [int(i) for i in input().split()]
print(V)


def sub_lists(arr, l):
    sublist = []
    for i in range(l + 1):
        for j in range(i + 1, l + 1):
            sub = arr[i:j]
            sublist.append(sub)
    return sublist


print(sub_lists(V, N))
sub = sub_lists(V, N)

sub_real = copy.deepcopy(sub)

def remove_dup(subs):

    for i in range(len(subs)):
        new = []
        for j in range(len(subs[i])):
            if subs[i][j] not in new:
                new.append(subs[i][j])
            else:
                sub_real[i][j] = "x"

remove_dup(sub)

refreshed = []

for i in range(len(sub_real)):
    temp = []
    for j in range(len(sub_real[i])):
        if sub_real[i][j] != "x":
            temp.append(sub_real[i][j])
    refreshed.append(temp)


sub_real = refreshed


for i in range(len(sub_real)):
    sub_real[i].sort()

print(sub_real)

result = 0
for i in range(len(sub_real)):
    for j in range(len(sub_real[i])):
            #sub_real[i].sort()
            result += (sub_real[i][j] * (sub_real[i].index(sub_real[i][j]) + 1))

print(result)
