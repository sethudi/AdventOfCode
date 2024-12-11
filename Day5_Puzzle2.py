import re
def main():
    
    dicPageOder ={}
    correctUpdates =[]
    incorrectUpdates =[]
    file = open("Day5_Input.txt")
    lines = file.readlines()

    i = 0
    while i< len(lines):
        if lines[i] == '\n':
            i += 1
            break
       
        one ,two =re.match(r'\S+',lines[i])[0].split('|')
        if one not in dicPageOder:
            dicPageOder[one] = set()
        dicPageOder[one].add(two)
        i += 1
            
    while i< len(lines):
        update = re.match(r'\S+',lines[i])[0].split(',')
        for j in range(1, len(update)):
            for k in range(j):
                if update[j] in dicPageOder and update[k] in dicPageOder[update[j]]:
                    isBreak = True
                    break
                else:
                    isBreak = False
            if isBreak:
                break
        if not isBreak:
            correctUpdates.append(update)
        else:
            incorrectUpdates.append(update)
        i += 1

    file.close()

    midPageSum =0
    for i in range(len(incorrectUpdates)):
        for j in range(1, len(incorrectUpdates[i])):
            for k in range(j):
                if incorrectUpdates[i][j] in dicPageOder and incorrectUpdates[i][k] in dicPageOder[incorrectUpdates[i][j]]:
                    incorrectUpdates[i][j], incorrectUpdates[i][k] = incorrectUpdates[i][k], incorrectUpdates[i][j]

    for incorrectUpdate in incorrectUpdates:
        midPageIdx = len(incorrectUpdate)//2
        midPageSum += int(incorrectUpdate[midPageIdx])
      
    print(len(incorrectUpdates), midPageSum)
    

if __name__ == "__main__":
    main()