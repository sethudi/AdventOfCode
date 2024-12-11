
def main():
    wordPuzzle =[]
    with open("Day4_Input.txt") as file:
        for line in file:
            # Parse the line into individual numbers
            row = list(line)
            if row[-1] == '\n':
                row.pop()
            wordPuzzle.append(row)

    count = 0
    compereX_MAS = {(('M','S'),'A',('S','M')), (('S','M'),'A',('M','S')), (('S','S'),'A',('M','M')), (('M','M'),'A',('S','S'))}
    # Find the starting point
    for i in range(len(wordPuzzle)):
        for j in range(len(wordPuzzle[0])):
            if wordPuzzle[i][j] == 'A':
                start = (i, j)
                if isPotentialX_MAS(wordPuzzle, start):
                    count += countX_MAS(wordPuzzle, start, compereX_MAS)

    return count

def isPotentialX_MAS(wordPuzzle, start):
    row, col = start
    return True if row -1 >= 0 and row +1 <len(wordPuzzle) and col -1 >= 0 and col +1 < len(wordPuzzle) else False

def countX_MAS(wordPuzzle, start, compereX_MAS):
    row, col = start
    compare1 = ((wordPuzzle[row+1][col-1],wordPuzzle[row-1][col-1]),'A',(wordPuzzle[row-1][col+1],wordPuzzle[row+1][col+1]))
    compare2 = ((wordPuzzle[row+1][col-1],wordPuzzle[row][col+1]),'A',(wordPuzzle[row-1][col+1],wordPuzzle[row][col-1]))
    compare3 = ((wordPuzzle[row][col-1],wordPuzzle[row-1][col-1]),'A',(wordPuzzle[row][col+1],wordPuzzle[row+1][col+1]))
    compare4 = ((wordPuzzle[row][col-1],wordPuzzle[row-1][col]),'A',(wordPuzzle[row][col+1],wordPuzzle[row+1][col]))
    isX_MAS = compare1 or compare2 or compare3 or compare4
    return 1 if isX_MAS in compereX_MAS else 0
        

    
if __name__ == '__main__':
    print(main())