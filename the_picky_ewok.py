import sys

n, r = [int(i) for i in sys.stdin.readline().split()]

powers = [0 for i in range(r)]
for i in range(r):
    f, p = [int(i) for i in sys.stdin.readline().split()]
    powers[i] = p

fib = [0, 1]
for i in range(r):
    fib[i] = fib[i - 1]

a_p = fib[n - 2]
b_p = fib[n - 1]

if (n == 1):
    a_p = 1
    b_p = 0
elif (n == 2):
    a_p = 0
    b_p = 1

for i in range(r):
    if ((a_p != 0 and powers[i] % a_p != 0) and (b_p != 0 and powers[i] % b_p != 0)):
       sys.stdout.write('NO')
       break
else:
    sys.stdout.write('YES')

sys.stdout.write('\n')