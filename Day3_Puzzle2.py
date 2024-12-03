import re
def main():
    result =0

    with open("Day3_Input.txt") as file:
        do =True
        for line in file:
            uncorruptedMul =re.findall(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))', line)
            for mul in uncorruptedMul:
                if re.match(r'^mul', mul, re.M) and do:
                    num1, num2 = map(int, re.findall(r'\d{1,3}', mul))
                    result += num1 * num2
                elif re.match(r'^do\(\)$', mul, re.M):
                    do =True
                elif re.match(r'^don\'t\(\)$', mul, re.M):
                    do =False
                    

    print(result)





if __name__ == '__main__':
    main()