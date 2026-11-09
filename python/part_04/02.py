n = int(input())
seq = list(map(int, input().split()))
dress_used = set()

for i in range(len(seq)):
    d = seq[i]
    if d not in dress_used:
        dress_used.add(d)
    if len(dress_used) == 3:
        print(i + 1)
        break
else:
    print(n)