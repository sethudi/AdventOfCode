
def main():
    positionGraph =[]

    with open("Day6_Input.txt") as file:
        for line in file:
            row = list(line)
            if row[-1] == '\n':
                row.pop()

            j = row.index('^') if '^' in row else 0
            if j:
                iRow = len(positionGraph)
                iCol = j

            positionGraph.append(row)

    return countDistinctPositions(positionGraph, iCol, iRow)


def countDistinctPositions(positionGraph, iCol, iRow):
    count = 0
    if positionGraph[iRow][iCol] == '^':
        direction = 'Up' 
    elif positionGraph[iRow][iCol] == '>':
        direction = 'Right'
    elif positionGraph[iRow][iCol] == '<':
        direction = 'Left'
    else:
        direction = 'Down'
    inBoardBoundries =iCol < len(positionGraph[0]) and iCol >=0 and iRow < len(positionGraph) and iRow >= 0

    while inBoardBoundries and positionGraph[iRow][iCol] != '#':

        if positionGraph[iRow][iCol] != 'X':
            count +=1
            positionGraph[iRow][iCol] = 'X'

        if direction == 'Up':
            iRow -= 1
        elif direction == 'Right':
            iCol += 1
        elif direction == 'Left':
            iCol -= 1
        else:
            iRow += 1

        inBoardBoundries =iCol < len(positionGraph[0]) and iCol >=0 and iRow < len(positionGraph) and iRow >= 0
        if inBoardBoundries and positionGraph[iRow][iCol] == '#':
            if direction == 'Up':
                direction = 'Right'
                iRow += 1
                iCol += 1
            elif direction == 'Right':
                direction = 'Down'
                iCol -= 1
                iRow += 1
            elif direction == 'Down':
                direction = 'Left'
                iRow -= 1
                iCol -= 1
            else:
                direction = 'Up'
                iCol += 1
                iRow -= 1

        inBoardBoundries =iCol < len(positionGraph[0]) and iCol >=0 and iRow < len(positionGraph) and iRow >= 0
    
    return count

if __name__=="__main__":
    print(main())