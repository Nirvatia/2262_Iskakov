x = [int(t) for t in input().split()]
i = 0
while i < len(x) and (x[i] < i or x[i] >= 2 * i) and (x[i] < 3 * i or x[i] >= 4 * i):
   i += 1
print(i)