k = int(input())
x_max = - (10 ** 9 + 1)
x_min = 10 ** 9 + 1
y_max = -(10 ** 9 + 1)
y_min = 10 ** 9 + 1
for _ in range(k):
	# x_max = - (10 ** 9 + 1)
	# x_min = 10 ** 9 + 1
	# y_max = -(10 ** 9 + 1)
	# y_min = 10 ** 9 + 1
	x, y = map(int, input().split())
	x_max = max(x, x_max)
	x_min = min(x, x_min)
	y_min = min(y, y_min)
	y_max = max(y, y_max)
print(x_min, y_min, x_max, y_max)