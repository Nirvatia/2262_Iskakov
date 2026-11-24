secret_word = input()

n = int(input())

magic_dict = {}

while n > 0:
    word_normal = input()
    word_similar = input()

    magic_dict[word_normal] = word_similar

    n -= 1

res = ""

for i in range(len(secret_word)):
    p1 = secret_word[0:i + 1]
    p2 = secret_word[i + 1:]

    if p1 in magic_dict and p2 in magic_dict:
        res = magic_dict[p1] + magic_dict[p2]
        break

print(res)