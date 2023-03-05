s = input()
stack = []
symbols = s.split()
for i in range(len(symbols)):
    if symbols[i] != '+' and symbols[i] != '-' and symbols[i] != '*':
        stack.append(int(symbols[i]))
    elif symbols[i] == '+':
        rhs = stack.pop()
        lhs = stack.pop()
        stack.append(lhs + rhs)
    elif symbols[i] == '*':
        rhs = stack.pop()
        lhs = stack.pop()
        stack.append(lhs * rhs)
    elif symbols[i] == '-':
        rhs = stack.pop()
        lhs = stack.pop()
        stack.append(lhs - rhs)
print(stack.pop())