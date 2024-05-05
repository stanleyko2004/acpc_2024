
import sys

x, t, v_h, v_g = [int(x) for x in sys.stdin.readline().split()]

t_h = 1000 / v_h
t_g = (1000 * 1000 + x * x) ** (1/2) / v_g

p = 'Han' if t_h + t > t_g else 'Greedo'

sys.stdout.write(p)
sys.stdout.write('\n')