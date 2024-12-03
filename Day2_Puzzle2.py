
def countSafeReports():
    count = 0
    unsafeReports = []

    with open("Day2_Input.csv") as file:
        for line in file:
            row =[int(num) for num in line.split()]

            if isSafeReport(row):
                count += 1
            else:
                unsafeReports.append(row)

    return removingLevelUnsafeReport(unsafeReports, count)

    
def removingLevelUnsafeReport(unsafeReports, count):
    
    for report in unsafeReports:  

        for i in range(len(report)):
            row = report.copy() 
            row.pop(i)

            if isSafeReport(row):
                count += 1
                break

    return count

def isSafeReport(row):
    isIncreasing = True if row[1] > row[0] else False
    for i in range(1, len(row)):
        if isIncreasing and not(row[i] > row[i-1] and abs(row[i] - row[i-1]) < 4):
            return False
        if not isIncreasing and not(row[i] < row[i-1] and abs(row[i] - row[i-1]) < 4):
            return False
        
    return True

        

if __name__ == "__main__":  
    print(countSafeReports())
    