import parse
import re

p = parse.get_input()
txt = [l for l in p.raw_text]

sum_elem = 0
sum_arr = []

for line in txt:
    if line != '':
        sum_elem += int(line)
    else:
        sum_arr.append(int(sum_elem))
        sum_elem = 0

print(max(sum_arr))

# Part 1
sum_arr.sort(reverse = True)

# Part 2
print(sum(sum_arr[:3]))