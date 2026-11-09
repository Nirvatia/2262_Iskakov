n = int(input())

conditions = ['1234567890', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm']

for i in range(n):
    p = input()
    if all(any(ch in c for ch in p) for c in conditions):
        print('strong')
    else:
        print('weak')