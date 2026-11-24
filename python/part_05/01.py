n, m = map(int, input().split())
seq = list(map(float, input(). split()))

def make_thing(arr):
    res = []

    for i, val in enumerate(arr):
        new_val = 0

        if i == 0:
            new_val = (2 * arr[0] + arr[1]) / 3
        elif i == len(arr) - 1:
            new_val = (2 * arr[i] + arr[i - 1]) / 3
        else:
            new_val = (arr[i - 1] + arr[i] + arr[i + 1]) / 3

        res.append(new_val)

    return res

while m > 0:
    seq = make_thing(seq)

    m -= 1

print(*seq)