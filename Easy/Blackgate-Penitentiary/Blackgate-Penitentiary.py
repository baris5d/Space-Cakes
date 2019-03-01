"""
Created by Bhasfe
01/03/2019
"""

n_members = int(input(""))
names_heights = dict()
while n_members>0:
    name,height= input("").split()
    names_heights[name] = height
    n_members-=1

new_dict = {}
for k, v in names_heights.items():
    new_dict.setdefault(v,[]).append(k)

heights_lists = []
for k in new_dict.keys():
    for t in range(len(new_dict[k])):
        heights_lists.append(k)

for i in sorted(new_dict.keys(),reverse=False):
    for j in sorted(new_dict[i]):
        print(j,end = " ")

    heights_lists.sort()
    print(heights_lists.index(i)+1,end=" ")
    print(heights_lists.index(i)+heights_lists.count(i))
