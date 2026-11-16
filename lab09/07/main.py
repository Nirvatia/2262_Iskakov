def every_other(seq):
    it = iter(seq)
    x = next(it, None)
    while x != None:
        yield x
        x = next(it, None)
        x = next(it, None)
    
print(*every_other([1,2,3,4,5]))

# Expected: 10 30 50
print (*every_other([10, 20, 30, 40, 50]))

# Expected: 0 2 4 6 8
print(*every_other(range(10)))

# Expected: 0 2 4 6 8
print(*every_other(iter(range(10))))

# Expected: 2 5 11 3 8
print(sum(every_other(map(int, input().split()))))