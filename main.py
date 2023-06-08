def parse(expression):
    res = []
    number = ''

    for i in expression:
        if i in "1234567890.":
            number += i
        elif number:
            res.append(float(number))
            number = ""
        if i in "+-*/()":
            res.append(i)
    if number:
        res.append(float(number))

    return res


def sortexpression(parsedexpression):
    res = []
    curexp = []
    for i in parsedexpression:
        if str(i) in "+-*/":
            # priority1 = "+-*/()".find(i)
            # priority2 = "+-*/()".find(curstack[-1])
            # while curstack and curstack[-1] != '(' and priority1 <= priority2:
            while curexp and curexp[-1] != '(' and "+-*/".find(i) <= "+-*/".find(curexp[-1]):
                res.append(curexp.pop())
            curexp.append(i)
        elif i == ')':
            while curexp:
                last = curexp.pop()
                if last == '(':
                    break
                res.append(last)
        elif i == '(':
            curexp.append(i)
        else:
            res.append(i)
    while curexp:
        res.append(curexp.pop())
    return res


def calculatepolish(sortedexpression):
    numbers = []
    for i in sortedexpression:
        if str(i) in "+-*/":
            second = numbers.pop()
            first = numbers.pop()
            res = 0

            # match str(i):
            #     case '+':
            #         res = first + second
            #     case '-':
            #         res = first - second
            #     case '*':
            #         res = first * second
            #     case '/':
            #         res = first / second

            if str(i) == '+':
                res = first + second
            elif str(i) == '-':
                res = first - second
            elif str(i) == '*':
                res = first * second
            elif str(i) == '/':
                res = first / second

            numbers.append(res)
        else:
            numbers.append(i)
    return numbers[0]


if __name__ == '__main__':
    print(calculatepolish(sortexpression(parse(str(input())))))
#     exp = parse(str(input()))
#     print(exp)
#     exp = sortexpression(exp)
#     print(exp)
#     exp = calculatepolish(exp)
#     print(exp)
# 12+(16+3*4-1)
# (1+2)*4-1