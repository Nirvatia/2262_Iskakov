s = input()

letters = {}
letter_to_remove = ''
best_cnt = 0

for i in s:
    if i in letters:
        letters[i] += 1
    else:
        letters[i] = 1
    if letters[i] > best_cnt:
        letter_to_remove = i
        best_cnt = letters[i]

res = s.replace(letter_to_remove, '')

print(res)
