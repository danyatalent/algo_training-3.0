word = input()
ans = [0] * 26
pos_freq = [0 for i in range(len(word))]
for i in range (len(word)):
    pos_freq[i] = (i + 1) * (len(word) - i)
    ans[ord(word[i]) - ord('a')] += pos_freq[i]
for i in range (len(ans)):
    if ans[i] != 0:
        print(chr(i + 97), end='')
        print(":", ans[i])
