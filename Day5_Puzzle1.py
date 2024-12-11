import re
def main():
    
    dicPageOder ={}
    correctUpdates =[]
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
        i += 1

    file.close()

    midPageSum =0

    for correctUpdate in correctUpdates:
        midPageIdx = len(correctUpdate)//2
        midPageSum += int(correctUpdate[midPageIdx])

    print(len(correctUpdate), midPageSum)
    

if __name__ == "__main__":
    main()