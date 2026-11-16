lst = ['hello', 'hell', 'bye', 'world', 'bybye']

lst.sort(key=lambda s: (len(s), s))

# Expected: ['bye', 'hell', 'babye', 'hello', 'world']
print(lst)