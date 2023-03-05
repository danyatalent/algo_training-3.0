n = int(input())
k = int(input())
m1 = int(input())
l1 = int(input())
k1 = (m1 - 1)*2 + l1
m2 = 10000000000
m3 = -10000000000
if k1 + k > n and k1 - k < 1:
    print(-1)
else:
    if k1 + k <= n:
        m2 = (k1 + k - 1)//2 + 1
        l2 = (k1 + k - 1)%2 + 1
    if k1 - k > 0:
        m3 = (k1 - k - 1)//2 + 1
        l3 = (k1 - k - 1)%2 + 1
    if m2 - m1 <= m1 - m3:     
        print(m2, l2)
    else:
        print(m3, l3)