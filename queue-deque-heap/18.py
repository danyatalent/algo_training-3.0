class Deque:
    def __init__(self):
        self.deque = []
    def empty(self):
        return self.deque == []
    def push_front(self, item):
        self.deque.append(item)
    def push_back(self, item):
        self.deque.insert(0, item)
    def pop_front(self):
        removed = self.deque.pop()
        return removed
    def pop_back(self):
        removed = self.deque.pop(0)
        return removed
    def size(self):
        return len(self.deque)
    def clear(self):
        self.deque.clear()
    def front(self):
        return self.deque[-1]
    def back(self):
        return self.deque[0]

dq = Deque()
s = input()
if s == 'exit':
    print('bye')
else:
    while s != 'exit':
        s = s.split()
        if s[0] == 'push_front':
            dq.push_front(int(s[1]))
            print('ok')
        elif s[0] == 'push_back':
            dq.push_back(int(s[1]))
            print('ok')
        elif s[0] == 'pop_front':
            if not dq.empty():
                print(dq.pop_front())
            else:
                print('error')
        elif s[0] == 'pop_back':
            if not dq.empty():
                print(dq.pop_back())
            else:
                print('error')
        elif s[0] == 'front':
            if not dq.empty():
                print(dq.front())
            else:
                print('error')
        elif s[0] == 'back':
            if not dq.empty():
                print(dq.back())
            else:
                print('error')
        elif s[0] == 'size':
            print(dq.size())
        elif s[0] == 'clear':
            dq.clear()
            print('ok')
        s = input()
    print('bye')