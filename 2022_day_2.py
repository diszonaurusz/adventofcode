import parse

p = parse.get_input(True)
txt = [t.split(' ') for t in p.raw_text]

# Part 1
translator = {
    "X":"A",
    "Y":"B",
    "Z":"C"
}
points = {
    "A": 1,
    "B": 2,
    "C": 3
}

evaluated =[(points.get(a), points.get(translator.get(b))) for a, b in txt]
final = [b + (6 if a % 3 + 1 == b else 3 if a == b else 0) for a, b in evaluated]  
print(sum(final))

#txt = [['A', 'Y'],['B', 'X'],['C', 'Z']]
# Part 2
point_sum = 0
for a, b in txt[:20]:
    match b:
        case 'X':
            # -1 % 3 = abs(-1) % 3
            pt = (points.get(a) - 2) % 3 + 1
        case 'Y':
            pt = points.get(a) + 3
        case 'Z':
            pt = points.get(a) % 3 + 7
    point_sum += pt
    print(a, b, points.get(a), pt, point_sum)
    
print(point_sum)  