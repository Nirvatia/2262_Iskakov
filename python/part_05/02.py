n = input()

seq = list(map(int, input(). split()))

seq = sorted(seq, key=lambda x: (abs(x), 1 if x >= 0 else 0))

print(*seq)