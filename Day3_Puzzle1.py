import re
def main():
    result =0

    with open("Day3_Input.txt") as file:
        for line in file:
            uncorruptedMul =re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
            for mul in uncorruptedMul:
                num1, num2 = map(int, re.findall(r'\d{1,3}', mul))
                result += num1 * num2

    print(result)

if __name__ == '__main__':
    main()