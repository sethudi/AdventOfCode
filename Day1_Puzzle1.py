

def foo():
    result = 0
    arrOne = []
    arrTwo = []
    

    with open("puzzle1_Input.csv") as file:
       for line in file:
            idOne, idTwo =line.split()
            arrOne.append(int(idOne))
            arrTwo.append(int(idTwo))

    arrOne.sort()
    arrTwo.sort()        

    for location1, location2 in zip(arrOne, arrTwo):
        result += abs(location1 - location2) 
    print(result)

foo()


# 30555275