
import sys

s = sys.stdin.readline()
n = int(sys.stdin.readline())

st = ["" for i in range(n)]
for i in range(n):
    st[i] = sys.stdin.readline()

for i in range(n):
    a = 0
    b = 0
    while a < len(s) and b < len(st[i]):
        if s[a] == st[i][b]:
            a += 1
            b += 1
        else:
            a += 1
    if b == len(st[i]):
        sys.stdout.write('YES')
    else:
        sys.stdout.write('NO') 
    sys.stdout.write('\n')

sys.stdout.write('\n')