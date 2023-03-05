stack = []
s = input()
flag = True
for i in range(len(s)):
    if s[i] == '(' or s[i] == '[' or s[i] == '{':
        stack.append(s[i])
    else:
        if len(stack) == 0:
            flag = False
        elif s[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                #print('no')
                break
        elif s[i] == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                #print('no')
                break
        elif s[i] == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                #print('no')
                break
if len(stack) == 0 and flag:
    print('yes')
else: print('no')