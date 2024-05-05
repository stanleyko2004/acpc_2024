import sys

n = int(sys.stdin.readline())

s = [(0, 0) for i in range(n)]
for i in range(n):
    w, h = [int(i) for i in sys.stdin.readline().split()]
    if h > w:
        s[i] = (h, w)
    else:
        s[i] = (w, h)
    
s = sorted(s)[::-1]

m = 0
bottom = 0
for (h, w) in s:
    bottom += w
    #if (bottom >= h):
    m = max(m, min(bottom, h))
sys.stdout.write(str(m)) 

sys.stdout.write('\n')