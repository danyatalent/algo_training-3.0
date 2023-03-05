a = list(map(int, input().split(':')))
b = list(map(int, input().split(':')))
c = list(map(int, input().split(':')))
a_sec = (a[0] * 60 + a[1]) * 60 + a[2]
b_sec = (b[0] * 60 + b[1]) * 60 + b[2]
c_sec = (c[0] * 60 + c[1]) * 60 + c[2]
if c_sec < a_sec: c_sec += 86400
delay = int((c_sec - a_sec) / 2) + 1 if (c_sec - a_sec) % 2 == 1 else int((c_sec - a_sec) / 2)
b_sec += delay
if b_sec > 86400: b_sec -= 86400
seconds = int(b_sec % 60)
minutes = int((b_sec - seconds) / 60)
hours = int(minutes // 60)
minutes %= 60
if hours < 10: hours = '0' + str(hours)
if minutes < 10: minutes = '0' + str(minutes)
if seconds < 10: seconds = '0' + str(seconds)

print(f'{hours}:{minutes}:{seconds}')