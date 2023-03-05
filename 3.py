import bisect
f = open('input.txt')
n = int(f.readline())
diego = sorted(list(set(list(map(int, f.readline().split())))))
k = int(f.readline())
collectors = list(map(int, f.readline().split()))
#print(diego)

if n == 0:
    print(0)
else:
    for i in range(k):
        ans = bisect.bisect_left(diego, collectors[i])
        print(ans)

