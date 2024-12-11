
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
    # Find the starting point
    for i in range(len(wordPuzzle)):
        for j in range(len(wordPuzzle[0])):
            if wordPuzzle[i][j] == 'X':
                start = (i, j)
                count +=countXMASHelper(start, wordPuzzle, -1, 0)
                count +=countXMASHelper(start, wordPuzzle, -1, -1)
                count +=countXMASHelper(start, wordPuzzle, -1, 1)
                count +=countXMASHelper(start, wordPuzzle, 0, 1)
                count +=countXMASHelper(start, wordPuzzle, 0, -1)
                count +=countXMASHelper(start, wordPuzzle, 1, 1)
                count +=countXMASHelper(start, wordPuzzle, 1, -1)
                count +=countXMASHelper(start, wordPuzzle, 1, 0)

    return count

def countXMASHelper(start, wordPuzzle, i, j):
    row, col = start
    row += i
    col += j
    word =['X']
    count =0
    while len(wordPuzzle)> row >=0 and len(wordPuzzle[0])> col >=0 and count < 3:
        word.append(wordPuzzle[row][col])
        row += i
        col += j
        count +=1

    return 1 if 'XMAS' == ''.join(word) else 0

    
if __name__ == '__main__':
    print(main())