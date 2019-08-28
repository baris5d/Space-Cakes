import sys

n = int(input())
scenerio = []
scenerios = []
baslangic = 1

def move(t,balls,d):
    for x in range(0,t):
        for b in range(0, len(balls)):
            balls[b][0] += balls[b][1]
            if balls[b][0] >= 100 or balls[b][0] <= 0:
                if b==(d-1):
                    # Eğer top istenilen index’se bunun konumunu döndür direkt
                    if balls[b][0]>=100:
                        return 100
                    else:
                        return 0
                else:
                    # eğer cebe girdiyse index'in dışına çıkart, bir daha hesaba katılmasın.
                    balls[b][0] = -10
                    balls[b][1] = 0
            if (b+1) < len(balls):
                if balls[b][1]>0 and balls[b][0]+1 >= balls[b+1][0] or balls[b][1]<0 and balls[b][0]-1 >= balls[b+1][0]: # bu kontrolde bir sorun var
                    #çarpıştıysa yönlerini değiştir.
                    balls[b][1] = 0 - balls[b][1]
                    balls[b+1][1] = 0 - balls[b+1][1]
    return balls[d-1][0]
  
for i in range(0,n):
    scenerio.append(list(map(int, input().split())))


for y in scenerio:
    for i in range(y[0]):
        scenerios.append([y[baslangic],y[baslangic+1]])
        baslangic += 2

    print(move(y[len(y)-1],scenerios,len(scenerios)))
    baslangic = 1
    scenerios = []
"""
for y in scenerio:    
    for i in range(y[0]):
        scenerios.append([scenerio[i][baslangic],scenerio[i][baslangic+1]])
        baslangic += 2
    time = y[len(y)-1]
    trackingBall = y[len(y)-2]
    print(move(time, scenerios,trackingBall),"\n")
    baslangic = 1 
    scenerios = []
"""