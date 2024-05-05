import sys

a, b = [int(i) for i in sys.stdin.readline().split()]

dp = {1: 1}
key = []
for i in range(1, int(a ** (1/2)) + 1):
    if a % i == 0:
        dp[i] = 1
        dp[ a // i] = 1
        key.append(i)
#print(dp)

#print(key)
key.append(a)
dp[a]=1

for i in range(len(key)):
    ##print('dpkeyi', dp[key[i]])
    ##print('keyi', key[i])
    if key[i] != 0 and key[i] != 1 and b % key[i] == 0:
        dp[key[i]] = 0
#print(dp)

for k in range(1, len(key)):
    for k_2 in range(k + 1, len(key)):
        if b % key[k_2] != 0 and key[k_2] % key[k] == 0:
            dp[key[k_2]] += dp[key[k]]
#print(dp)
sys.stdout.write(str(dp[a]))
sys.stdout.write('\n')