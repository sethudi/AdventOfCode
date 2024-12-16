import re
def main():
    mapHiking = []
    # Read input file
    with open('Day10_Input.txt') as file:
        for line in file:
            row = list(re.match(r'.*',line)[0])
            mapHiking.append(list(map(int,row)))

    count = 0
    for i in range(len(mapHiking)):
        for j in range(len(mapHiking)):
            if mapHiking[i][j] == 0:
                count += countHikingTrail(mapHiking, i, j, 0)

    print("count: ", count)        

def countHikingTrail(mapHiking, i, j, height):
    if not(i >=0 and i < len(mapHiking) and j >=0 and j < len(mapHiking[0])) or mapHiking[i][j] != height:
           return 0
    
    if mapHiking[i][j] == 9:
        return  1

    count =0
    for row, col in [(i-1,j), (i,j +1), (i +1,j), (i,j -1)]:
        count += countHikingTrail(mapHiking, row, col, height +1)

    return count

if __name__ == '__main__':
    main()