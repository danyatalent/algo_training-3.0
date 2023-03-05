n = int(input())
price = list(map(int, input().split()))
stack = []
ans = [0] * n
for i in range(len(price)):
    if len(stack) == 0:
        stack.append(i)
    elif price[i] < price[stack[-1]]:
        while len(stack) != 0 and price[stack[-1]] > price[i]:
            index = stack.pop()
            ans[index] = i
        stack.append(i)
    else:
        stack.append(i)
for i in range(len(stack)):
    index = stack[i]
    ans[index] = -1
print(*ans)