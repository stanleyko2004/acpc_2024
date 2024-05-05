import sys

n = int(sys.stdin.readline())

h = [0] + [int(x) for x in sys.stdin.readline().split()]
m = 0
for i in range(len(h)-1):
    m = max(m, h[i+1]-h[i])

sys.stdout.write(str(m))
sys.stdout.write('\n')

# for i in range(t):
#     [n, k] = [int(x) for x in sys.stdin.readline().split()]
#     c = [int(x) for x in sys.stdin.readline().split()]
#     freq = {}
#     for i in c:
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1
#     if (max(freq.values()) >= k):
#         sys.stdout.write(str(k-1))
#     else:
#         sys.stdout.write(str(n))
#     sys.stdout.write('\n')
