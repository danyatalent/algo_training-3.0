subs = int(input())
s = input()
alph = 'abcdefghijklmnopqrstuvwxyz'
_max = 0
for letter in alph:
    k = subs
    right = 0
    for left in range(len(s)):
        if left > 0 and s[left - 1] != letter:
            k += 1
        while k >= 0 and right != len(s):
            if s[right] != letter:
                if k != 0: k -= 1
                else: break
            right += 1
        _max = max(right - left, _max)
        if right == len(s): break
print(_max)