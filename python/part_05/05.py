from math import sqrt

w, h, s = map(int, input().split())

sections = (w + s - 1) // s
last_section_width = w % s

dots = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    dots.append([x, y])

section_dots = [[] for _ in range(sections)]

# k*s ≤ x < (k+1)*s
# k ≤ x/s < k+1
# по сути становится k = floor(x / s)

for d in dots:
    k = d[0] // s
    section_dots[k].append(d)

for i, _ in enumerate(section_dots):
    if i % 2 == 0:
        section_dots[i] = sorted(section_dots[i], key=lambda e: (e[1], e[0]))
    else:
        section_dots[i] = sorted(section_dots[i], key=lambda e: (-e[1], e[0]))

prev_dot = section_dots[0][0]
res = 0

for i in range(sections):
    for j in range(len(section_dots[i])):
        if i == 0 and j == 0:
            continue

        curr_dot = section_dots[i][j]
        dist = sqrt((prev_dot[0] - curr_dot[0]) ** 2 + (prev_dot[1] - curr_dot[1]) ** 2)
        prev_dot = curr_dot

        res += dist

print(res)



