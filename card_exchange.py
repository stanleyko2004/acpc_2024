import sys

t = int(sys.stdin.readline())

for i in range(t):
    [n, k] = [int(x) for x in sys.stdin.readline().split()]
    c = [int(x) for x in sys.stdin.readline().split()]
    freq = {}
    for i in c:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    if (max(freq.values()) >= k):
        sys.stdout.write(str(k-1))
    else:
        sys.stdout.write(str(n))
    sys.stdout.write('\n')
