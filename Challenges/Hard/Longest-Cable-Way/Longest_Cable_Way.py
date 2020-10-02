# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:32:34 2019

@author: Acan
"""

# Longest cable way problem
# The trick is the optimal composition for the end section after k*Max_Stick or 
# after (k-1)*Max_Stick.

import numpy as np

"""
D=int(input("Enter the total cable length as an integer"))

Rod_Inventory=[]

# Read stick lengths
x,y=input("Enter the number of stick size and the amonut in inventory stock, separated by space").split(' ')

x=int(x)
y=int(y)

while not(x==0 and y==0):
    Rod_Inventory.append((x,y))
    
    x,y=input("Enter the number of stick size and the amonut in inventory stock, separated by space").split(' ')

    x=int(x)
    y=int(y)
    
Rod_Inventory.sort(reverse=True)
"""

D=577
Rod_Inventory={50:10, 45:12, 30:3, 16:2, 8:12, 3:2, 2:2}

"""
D=44
Rod_Inventory={30:31, 50:10, 45:12, 90:21, 43:1}
"""

Rod_Lengths=list(Rod_Inventory.keys())
Rod_Counts=list(Rod_Inventory.values())

Pop_Size=100
Pop=np.zeros(shape=(Pop_Size,len(Rod_Inventory)))
Total_Length=np.zeros(shape=(Pop_Size,1))
Num_Rods=np.zeros(shape=(Pop_Size,1))

K=D // Rod_Lengths[0]

for i in range(Pop_Size):
    for j in range(len(Rod_Inventory)):
        Pop[i,j]=round(min(2,Rod_Counts[j])*np.random.rand())
        
for i in range(Pop_Size):
    Total_Length[i]=(K-2)*Rod_Lengths[0]+sum([Pop[i,j]*Rod_Lengths[j] for j in range(len(Rod_Lengths))])
    Num_Rods[i]=(K-2)+Pop[i,0]+sum(Pop[i,1:])

Old_Pop=Pop
Old_Total_Length=Total_Length
Old_Num_Rods=Num_Rods

# Forward Iterative Improvements

Opt_Check=False
   
for i in range(Pop_Size):
    if Total_Length[i] > D:
        # Forward Pass
        Excess_Length=Total_Length[i]-D
        j=0
        Num_Rods_Removed=0
        while Excess_Length > 0 and j < len(Rod_Lengths):
            if (Rod_Lengths[j] <= Excess_Length) and (Pop[i,j] > 0):
                Excess_Length=Excess_Length-Rod_Lengths[j]
                Num_Rods_Removed=Num_Rods_Removed+1
                Pop[i,j]=Pop[i,j]-1
            else:
                j=j+1
        Total_Length[i]=D+Excess_Length
        Num_Rods[i]=Num_Rods[i]-Num_Rods_Removed
        
        if Excess_Length==0:
            Opt_Check=True            
            print("Iterative improvement successful")

if Opt_Check:            
    Opt_Length_Indexes=np.where(Total_Length == D)[0]
    MinNum_Rods=Num_Rods[Opt_Length_Indexes[0]]
    MinRod_Index=Opt_Length_Indexes[0]
    
    for i in Opt_Length_Indexes:
        if Num_Rods[i] < MinNum_Rods:
            MinNum_Rods=Num_Rods[i]
            MinRod_Index=i;
            
    
    print("Minimum Number of Rods Needed = ", MinNum_Rods)
    Pop[MinRod_Index,0] += (K-2)
    print("The Corresponding Solution is ", Pop[MinRod_Index])
else:
    print("No Solution")
    
"""
for i in range(Pop_Size):
    if Total_Length[i] > D:
        # Back Pass
        Excess_Length=Total_Length[i]-D
        j=len(Rod_Lengths)-1
        Num_Rods_Removed=0
        while Excess_Length > 0 and j >= 0:
            if (Rod_Lengths[j] <= Excess_Length) and (Pop[i,j] > 0):
                Excess_Length=Excess_Length-Rod_Lengths[j]
                Num_Rods_Removed=Num_Rods_Removed+1
                Pop[i,j]=Pop[i,j]-1
            else:
                j=j-1
        Total_Length[i]=D+Excess_Length
        Num_Rods[i]=Num_Rods[i]-Num_Rods_Removed
        
        if Excess_Length==0:
            print("Iterative improvement successful: ",i)               
  """
      