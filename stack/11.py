stack = []
s = input()
if s == 'exit':
    print('bye')
else:
    while s != 'exit':
        s = s.split()
        if s[0] == 'push':
            stack.append(int(s[1]))
            print('ok')
        elif s[0] == 'pop':
            if len(stack) > 0:
                print(stack.pop())
            else:
                print('error')
        elif s[0] == 'back':
            if len(stack) > 0:
                print(stack[-1])
            else:
                print('error')
        elif s[0] == 'size':
            print(len(stack))
        elif s[0] == 'clear':
            stack.clear()
            print('ok')
        s = input()
    print('bye')