import sys

n = int(sys.stdin.readline()) 

songs = {}
for i in range(n):
    [group, num_str] = sys.stdin.readline().split()
    songs[group] = int(num_str)
    
m = int(sys.stdin.readline())
likes = {}
for i in range(m):
    group = sys.stdin.readline().strip()
    if group in likes:
        likes[group] += 1
    else:
        likes[group] = 1

for group in songs.keys():
    if (songs[group] > likes[group]):
        sys.stdout.write(group)
        break
else:
    sys.stdout.write('NO KPOP FOR VADER')

sys.stdout.write('\n')