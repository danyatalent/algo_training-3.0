stack = []
n = int(input())
trains = list(map(int, input().split()))
ans = []
for i in range(len(trains)):
    if len(stack) == 0:
        stack.append(trains[i])
    elif stack[-1] > trains[i]:
        stack.append(trains[i])
    else:
        while(len(stack) != 0 and stack[-1] < trains[i]):
            ans.append(stack.pop())
        stack.append(trains[i])
ans += list(reversed(stack))
if ans == sorted(trains):
    print('YES')
else:
    print('NO')