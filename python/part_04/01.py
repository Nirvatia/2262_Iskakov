def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

n = int(input())

if n == 1:
    print(2)
else:
    cnt = 1
    curr = 3
    while cnt < n:
        if is_prime(curr):
            cnt += 1
        if cnt < n:
            curr += 2
    print(curr)
