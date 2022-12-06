import parse

p = parse.get_input(True)

txt = [t.split(' ') for t in p.raw_text]

# Part 1
vertical = [int(val) if typ == 'down' else int(val) * (-1) if typ == 'up' else 0 for typ, val in txt]
horizontal = [int(val) if typ == 'forward' else 0 for typ, val in txt]

print(sum(vertical) * sum(horizontal))

# Part 2
aim         = 0
horizontal  = 0
vertical    = 0

for (typ, val) in txt:
    if typ == 'up':
        aim -= int(val)
    if typ == 'down':
        aim += int(val)
    if typ == 'forward':
        horizontal += int(val)
        vertical += int(val) * aim

print(f'{horizontal} * {vertical} = {horizontal * vertical}')