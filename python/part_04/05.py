cards = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

key_type = input()
turns = int(input())

for i in range(turns):
    h1 = input().split()
    h2 = input().split()

    h1_value = cards[h1[0]]
    h1_type = h1[1]

    h2_value = cards[h2[0]]
    h2_type = h2[1]

    if h1_type == h2_type:
        if h2_value > h1_value:
            print(1, end=' ')
        else:
            print(0, end=' ')
    elif h1_type != h2_type and h2_type == key_type:
        print(1, end=' ')
    else:
        print(0, end=' ')

