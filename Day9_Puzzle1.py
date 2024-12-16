import re
def main():

    # Read input file
    with open('Day9_Input.txt') as file:
        for line in file:
            disk = [int(num) for num in list(re.match(r'.*',line)[0])]

    blocks = []  
    iD =0      
    for i, num in enumerate(disk):
        if i == 0:
            for j in range(num):
                blocks.append(str(iD))
            iD += 1
        elif i % 2 != 0:
            for j in range(num):
                blocks.append('.')
        else:
            for j in range(num):
                blocks.append(str(iD))
            iD += 1

    swapBlocksWithSpaces(blocks)
    getFileSystemCheckSum(blocks)

def getFileSystemCheckSum(blocks):
    checksum = 0
    for i, num in enumerate(blocks):
        checksum += i * int(num) if num != '.' else 0

    print(checksum)
    

def swapBlocksWithSpaces(blocks):
    left, right = 0, len(blocks)-1

    while left < right:
        while blocks[left] != '.' and left < right:
            left += 1
        while blocks[right] == '.' and right > left:
            right -= 1

        if left < right:
            blocks[left], blocks[right] = blocks[right], blocks[left]

    
if __name__ == '__main__':
    main()