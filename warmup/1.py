import sys


def printchart(s):
    symcount = {}
    maxsymcount = 0
    for sym in s:
        if sym not in symcount:
            symcount[sym] = 0
        symcount[sym] += 1
        maxsymcount = max(maxsymcount, symcount[sym])
    sorteduniqsyms = sorted(symcount.keys())
    for row in range(maxsymcount, 0, -1):
        for sym in sorteduniqsyms:
            if symcount[sym] >= row:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(sorteduniqsyms))

s = sys.stdin.read()
s = s.replace('\n', '')
s = s.replace(' ', '')
printchart(s)
