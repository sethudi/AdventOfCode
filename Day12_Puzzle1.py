import re
def main():
    gardenArea = []
    # Read input file
    with open('Day12_Input.txt') as file:
        for line in file:
            row = list(re.match(r'.*',line)[0])
            gardenArea.append(row)

    TotalPrice = 0
    isVisited = set()
    for i in range(len(gardenArea)):
        for j in range(len(gardenArea[0])):
            if (i, j) not in isVisited:
                parameter= getParameter(gardenArea, i, j, set(), gardenArea[i][j], 1)
                area = getArea(gardenArea, i, j, isVisited, gardenArea[i][j])
                print(gardenArea[i][j], area, parameter)
                TotalPrice += area *parameter

    print("TotalPrice: ", TotalPrice)        

def getArea(gardenArea, i, j, isVisited, plot):
    if not(i >=0 and i < len(gardenArea) and j >=0 and j < len(gardenArea[0])) or gardenArea[i][j] != plot:
           return 0
    
    isVisited.add((i, j))

    area =0
    for row, col in [(i-1,j), (i,j +1), (i +1,j), (i,j -1)]:
        if (row, col) not in isVisited:
            area +=getArea(gardenArea, row, col, isVisited, plot)

    return area +1

def getParameter(gardenArea, i, j, isVisited, plot, countPlot):
    if not(i >=0 and i < len(gardenArea) and j >=0 and j < len(gardenArea[0])) or gardenArea[i][j] != plot:
           return 1
    
    isVisited.add((i, j))

    parameter =0
    for row, col in [(i-1,j), (i,j +1), (i +1,j), (i,j -1)]:
        if (row, col) not in isVisited:
            parameter +=getParameter(gardenArea, row, col, isVisited, plot, countPlot+1)

    return parameter


if __name__ == '__main__':
    main()