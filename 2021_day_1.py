import get_input as inp

r = inp.get_input()
txt = [eval(i) for i in r.raw_text]

#Part 1
increase = 0

for i, item in enumerate(txt[1:],1):
    if txt[i - 1] < txt[i]:
        increase += 1

print(increase)

#Part 2
increase = 0
window_list = []

for i, item in enumerate(txt, 0):
    window_list.append(sum(txt[i:i + 3]))

for i, item in enumerate(window_list, 0):
    if window_list[i - 1] < window_list[i]:
        increase += 1

print(increase)