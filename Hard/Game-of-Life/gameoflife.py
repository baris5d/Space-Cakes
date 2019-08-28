## Baris Dede
# Conway's Game of Life

line = input().split()
iteration = int(line[2])
matrix = [] 

width = int(line[1])
height = int(line[0])

for i in range(height):          
    matrix.append(list(input())) 

# Hücrede yaşam var mı?
def isPopulated(ver,hor):
        return matrix[ver][hor]=="*"

# Komşu sayısını hesapla
def getNeighbourCount(y,x):
        count = 0
        
        top = height - 1 if y == 0 else y - 1
        bottom = 0 if y == height - 1 else y + 1

        left = width - 1 if x == 0 else x - 1
        right = 0 if x + 1 == width else x + 1

        # top left
        count += 1 if isPopulated(top,left) == 1 else 0
        # top middle
        count += 1 if isPopulated(top,x)  == 1 else 0
        # top right
        count += 1 if isPopulated(top,right)  == 1 else 0
        # left
        count += 1 if isPopulated(y,left)  == 1 else 0
        # right
        count += 1 if isPopulated(y,right)  == 1 else 0
        # bottom left
        count += 1 if isPopulated(bottom,left)  == 1 else 0
        # bottom middle
        count += 1 if isPopulated(bottom,x)  == 1 else 0
        # bottom right
        count += 1 if isPopulated(bottom,right)  == 1 else 0
        
        return count

# Bir sonraki kare için taslak oluştur        
def createTemplate(w, h): 
        tmp = []
        for i in range(h):
                tmp.append([])
                for x in range(w):
                        tmp[i].append('-')
                
        return tmp 

temp = createTemplate(width, height)
# 'iteration' kadar yaşa
for f in range(iteration):        
        for y in range(height):
                for x in range(width):
                        neighbourCount = getNeighbourCount(y,x)
                        if isPopulated(y,x) == 1:
                                if neighbourCount < 2 or neighbourCount > 3:
                                        #Hücreyi öldür
                                        temp[y][x] = "-"
                                else:
                                        #Hayatta kal
                                        temp[y][x] = "*"
                        else:
                                if neighbourCount == 3:
                                        #Yaşam başlat
                                        temp[y][x] = "*"
        matrix = temp
        temp = createTemplate(width, height)
for k in range(height):
        for l in range(width):
                print(matrix[k][l], end="")
        print()