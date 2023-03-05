def heapifyDown(lst, index, upper):
    while True:
        if max(index * 2 + 1, index * 2 + 2) < upper:
            if lst[index] >= max(lst[index * 2 + 1], lst[index * 2 + 2]):
                break
            elif lst[index * 2 + 1] > lst[index * 2 + 2]:
                lst[index], lst[index * 2 + 1] = \
                    lst[index * 2 + 1], lst[index]
                index = index * 2 + 1
            else:
                lst[index], lst[index * 2 + 2] = \
                    lst[index * 2 + 2], lst[index]
                index = index * 2 + 2
        elif index * 2 + 1 < upper:
            if lst[index * 2 + 1] > lst[index]:
                lst[index], lst[index * 2 + 1] = \
                    lst[index * 2 + 1], lst[index]
                index = index * 2 + 1
            else:
                break
        elif index * 2 + 2 < upper:
            if lst[index * 2 + 2] > lst[index]:
                lst[index], lst[index * 2 + 2] = \
                    lst[index * 2 + 2], lst[index]
                index = index * 2 + 2
            else:
                break
        else:
            break


def heapsort(lst):
    for j in range((len(lst) - 2) // 2, -1, -1):
        heapifyDown(lst, j, len(lst))
    
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        heapifyDown(lst, 0, end)

n = int(input())
lst = list(map(int, input().split()))
heapsort(lst)
print(*lst)