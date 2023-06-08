

def parse(input):
    res = []
    number = ''

    for i in input:
        if i in "1234567890.":
            number += i
        elif number:
            res.append(float(number))
            number = ""
        if i in "+-*/()":
            res.append(i)
    if number:
        res.append(number)

    return res


def sortExp(input):
    res = []
    curstack = []
    for i in input:
        if str(i) in "+-*/":
            # priority1 = "+-*/()".find(i)
            # priority2 = "+-*/()".find(curstack[-1])
            # while curstack and curstack[-1] != '(' and priority1 <= priority2:
            while curstack and curstack[-1] != '(' and "+-*/".find(i) <= "+-*/".find(curstack[-1]):
                res.append(curstack.pop())
            curstack.append(i)
        elif i == ')':
            while curstack:
                last = curstack.pop()
                if last == '(':
                    break
                res.append(last)
        elif i == '(':
            curstack.append(i)
        else:
            res.append(i)
    while curstack:
        res.append(curstack.pop())
    return res


if __name__ == '__main__':
    exp = parse(str(input()))
    print(exp)
    exp = sortExp(exp)
    print(exp)
#    print(exp[-1])
# 12+(16+3*4-1)
# (1+2)*4-1
