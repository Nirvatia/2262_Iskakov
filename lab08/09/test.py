def t(i):
   return i>=1000

left = -1
right = 10**18

print("=======================================")
print("Инвариант до входа в цикл: ", not t(left) and t(right))
print("=======================================")

i = 0

while right - left > 1:
   mid = left + (right - left) // 2
   if t(mid):
      right = mid
   else:
      left = mid
   print(f"Инвариант на итерации {i}: {not t(left) and t(right)}")
   i += 1

print("=======================================")
print("Инвариант после выхода из цикла: ", not t(left) and t(right))
print("=======================================")

print(right)