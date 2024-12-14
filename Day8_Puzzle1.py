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
                
                count +=isAntinode( area, x1, y1, x2, y2,isVisited)
                count +=isAntinode( area, x2, y2, x1, y1, isVisited)     

    print('final count:', count)

def isAntinode(area, x1, y1, x2, y2,isVisited):
    
    count = 0
    if x1 <= x2 and x1 - abs(x2 -x1) >= 0:
        isNorthWestAntinode =  y1 < y2 and y1 -abs(y2 -y1) >= 0
        isNorthEastAntinode =  y1 >= y2 and y1 +abs(y1 -y2) < len(area[0])

        newX = x1 - abs(x2 -x1)
        newY = y1 -abs(y2 -y1)
        if isNorthWestAntinode and (newX, newY) not in isVisited:
            isVisited.add((newX, newY))
            count +=1
        
        newY =y1 +abs(y1 -y2)
        if isNorthEastAntinode and (newX, newY) not in isVisited:
            isVisited.add((newX, newY)) 
            count +=1
    
    if x1 <= x2 and x2 +abs(x2 -x1) < len(area):
        isSouthWestAntinode =y1 > y2 and y2 - abs(y2 -y1) >= 0
        isSouthEastAntinode =y1 <= y2 and y2 +abs(y1 -y2) < len(area[0])

        newX = x2 +abs(x2 -x1)
        newY = y1 -abs(y2 -y1)
        if isSouthWestAntinode and (newX, newY) not in isVisited:
            isVisited.add((newX, newY))
            count +=1
        
        newY = y1 +abs(y2 -y1)
        if isSouthEastAntinode and (newX, newY) not in isVisited:
            isVisited.add((newX, newY)) 
            count +=1

    return count

if __name__ == "__main__":
    main()