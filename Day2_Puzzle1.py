
count = 0

with open("Day2_Input.csv") as file:
    for line in file:
        row =[int(num) for num in line.split()]

        isIncreasing = True if row[1] > row[0] else False
        for i in range(1, len(row)):
            if isIncreasing and not(row[i] > row[i-1] and abs(row[i] - row[i-1]) < 4):
                count -= 1
                break

            if not isIncreasing and not(row[i] < row[i-1] and abs(row[i] - row[i-1]) < 4):
                count -= 1
                break

        count += 1

print(count)
    