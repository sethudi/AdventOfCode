

def foo():
    result = 0
    arrOne = []
    arrTwo = []
    uniqueLocationsCount ={}

    with open("puzzle1_Input.csv") as file:
       for line in file:
            idOne, idTwo =line.split()
            arrOne.append(int(idOne))
            arrTwo.append(idTwo)       

    for locationID in  arrTwo:
        if locationID not in uniqueLocationsCount:
            uniqueLocationsCount[locationID] = 0
        uniqueLocationsCount[locationID] += 1

    for locationID in arrOne:
        if str(locationID) in uniqueLocationsCount:
            result += locationID * uniqueLocationsCount[str(locationID)]
            
    print(result)

foo()


