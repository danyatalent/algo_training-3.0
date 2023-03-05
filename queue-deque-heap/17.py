class Queue:
    def __init__(self):
        self.queue = []
    
    def push(self, item):
        self.queue.append(item)
    
    def pop(self):
        removed = self.queue.pop(0)
        return removed
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[0]
    
    def clear(self):
        self.queue.clear()

    def empty(self):
        return self.queue == []


f = Queue()
s = Queue()

s1 = input()
s2 = input()
s1 = s1.split()
s2 = s2.split()
for i in range(5):
    f.push(int(s1[i]))
    s.push(int(s2[i]))

step = 0
while (not (f.empty()) and not (s.empty()) and step + 1 < 10 ** 6):
    a = f.pop()
    b = s.pop()

    if (a > b and not (a == 9 and b == 0) or (a == 0 and b == 9)):
        f.push(a)
        f.push(b)
    if b > a and not (b == 9 and a == 0) or (b == 0 and a == 9):
        s.push(a)
        s.push(b)
    step += 1
    
if f.empty():
    print(f'second {step}')
elif s.empty():
    print(f'first {step}')
else:
    print('botva\n')
