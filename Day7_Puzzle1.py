import re
def main():
    equations = []
    with open('Day7_Input.txt') as file:
        for line in file:
            row = re.match(r'.*',line)[0].split(' ')
            row[0] = re.match(r'\d*',row[0])[0]
            equations.append(list(map(int,row)))

    sum = 0
    for equation in equations:
        if isTrueEquations(equation, 2, equation[1]):
            sum += equation[0]

    return sum

def isTrueEquations(equation, idx, total):
   
    if idx == len(equation):
        return total == equation[0]
    
    return isTrueEquations(equation, idx+1, total + equation[idx]) or isTrueEquations(equation, idx+1, total * equation[idx])

    # for operator in ['+', '*']:
    #     if operator == '+':
    #         if isTrueEquations(equation, idx+1, total + equation[idx]):
    #             return True
    #     elif operator == '*':
    #         if isTrueEquations(equation, idx+1, total * equation[idx]):
    #             return True
            
    # return False

if __name__ == "__main__":
    print(main())