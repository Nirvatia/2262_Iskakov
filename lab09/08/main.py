lst = [1,'abc', 2, 3, 4, 'aa']
nums = [el for el in lst if type(el) == int]

# Expected: [1, 2, 3, 4]
print(nums)