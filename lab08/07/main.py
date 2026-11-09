seq = map(int, input().split())

for i in seq:
    if i < 0:
        print(i)
        break
else:
    print("Отрицательных чисел не найдено.")

