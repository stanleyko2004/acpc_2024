import sys

s = sys.stdin.readline().strip()
f = sys.stdin.readline().strip()
n = len(s)
m = len(f)

dp = [[0 for i in range(m)] for j in range(n)]

if s[0] == f[0]:
    dp[0][0] = 1
if s[1] == f[0]:
    dp[1][0] = 1

def in_bounds(i):
    return 0 <= i and i < n

for i in range(1, n):
    for j in range(1, m):
        if s[i] == f[j]:
            a = 0
            b = 0
            if i > 1:
                a = dp[i - 2][j - 1]
            b = dp[i - 1][j - 1]
            dp[i][j] = (a + b) % 1000000007

res = (dp[n - 1][m - 1] + dp[n - 2][m - 1]) % 1000000007
sys.stdout.write(str(res))
sys.stdout.write('\n')