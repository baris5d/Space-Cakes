# XTREME DRIVING
import numpy as np

#L=28  # Length of the highway
#N=2  # Number of cows
#Cows=[[3,10],[2,10]]  # from the left side reference

L=5
N=2
Cows=[[1,2],[2,3]]

HighWay=np.zeros(shape=(4,L))

# Place  the cows
for Cow in Cows:
    HighWay[Cow[0]-1,Cow[1]-1]=-1       # -1 means that cell is occupied by a cow
    
# Car is initalli in leftmost lane
HighWay[0,0]=1

# Start the travel and record how many different ways each cell is visited
for j in range(1,L):
    for i in range(4):
        if i==0 and HighWay[i,j] ==0:
            if HighWay[i,j-1]>0:
                HighWay[i,j] += HighWay[i,j-1]
            if HighWay[i+1,j-1]>0:
                HighWay[i,j] += HighWay[i+1,j-1]
        elif i==3 and HighWay[i,j] ==0:
            if HighWay[i,j-1]>0:
                HighWay[i,j] += HighWay[i,j-1]
            if HighWay[i-1,j-1]>0:
                HighWay[i,j] += HighWay[i-1,j-1]
        elif HighWay[i,j]==0:
            if HighWay[i-1,j-1]>0:
                HighWay[i,j] += HighWay[i-1,j-1]
            if HighWay[i,j-1]>0:
                HighWay[i,j] += HighWay[i,j-1]                       
            if HighWay[i+1,j-1]>0:
                HighWay[i,j] += HighWay[i+1,j-1]
                
print(HighWay[0,L-1] % (10**+9 + 7))