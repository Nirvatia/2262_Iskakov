def sublist(a, *args):
    return [a[i] for i in args]

lst = ['Anna', 'Barbara', 'Clara', 'Diana', 'Eva', 'Flora']
# Expected: ['Anna', 'Clara', 'Flora']
print(sublist(lst, 0, 2, 5))

# Expected: []
print(sublist(lst))

# Expected: ['Anna', 'Barbara', 'Clara', 'Diana', 'Eva', 'Flora']
print(sublist(lst, 0, 1, 2, 3, 4, 5))