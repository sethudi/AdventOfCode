import re

def main():
    # Read input file
    with open('Day11_Input.txt') as file:
        for line in file:
            numbers = re.match(r'.*',line)[0].split(' ')

    print(numbers)
    for _ in range(25):
        listAfterBlink = []
        for num in numbers:
            if len(num) % 2 == 0:
                idx = len(num) //2
                listAfterBlink.append(num[:idx])
                listAfterBlink.append(str(int(num[idx:])))
            elif num == '0':
                listAfterBlink.append('1')
            else:
                listAfterBlink.append(str(int(num)*2024))
        
        numbers = listAfterBlink 

    print(len(numbers))       

if __name__ == '__main__':
    main()