import re
def main():
    area = []
    antennas = {}
    isVisited =set()

    with open('Day8_input.txt') as file:
        for line in file:
            row = re.match(r'.*', line)[0]
            area.append(list(row))

    for i in range(0, len(area)):
        for j in range(0, len(area[0])):
            char = area[i][j]

            if char != '.' :
                if char not in antennas:
                    antennas[char] = []

                antennas[char].append((i, j))
    count = 0

    for char, locations in antennas.items():
        for i in range(len(locations) -1):
            for j in range(i+1, len(locations)):
                x1, y1 = locations[i]
                x2, y2 = locations[j]
                
                count +=isAntinode( area, x1, y1, x2, y2, isVisited)
                count +=isAntinode( area, x2, y2, x1, y1, isVisited)     

    print('final count:', count)

def isAntinode(area, x1, y1, x2, y2,isVisited):
    xdistance = abs(x2 -x1)
    ydistance = abs(y2 -y1)

    count = 0
    isNothAntinode =x1 <= x2 
    
    if isNothAntinode:
        newX = x1 
        newY = y1 
        if y1 < y2:
            while newY >= 0 and newX>= 0:
                
                if (newX, newY) not in isVisited: 
                    isVisited.add((newX, newY))
                    count +=1
                
                newX -= xdistance
                newY -= ydistance
        else: 
            while newY < len(area[0]) and newX>= 0:
                
                if (newX, newY) not in isVisited:
                    isVisited.add((newX, newY))
                    count +=1
                
                newX -= xdistance
                newY += ydistance
    
    isSouthAntinode = x1 <= x2 

    if isSouthAntinode:
        newX = x2 
        newY = y2
        if y1 > y2:
            while newY >= 0 and newX < len(area):
                
                if (newX, newY) not in isVisited:
                    isVisited.add((newX, newY))
                    count +=1
                
                newX += xdistance
                newY -= ydistance
        else: 
            while newY < len(area[0]) and newX < len(area):
                
                if (newX, newY) not in isVisited:
                    isVisited.add((newX, newY))
                    count +=1
                
                newX += xdistance
                newY += ydistance

    return count

if __name__ == "__main__":
    main()