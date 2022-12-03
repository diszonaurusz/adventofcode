import get_input as inp
import re

r = inp.get_input()

txt = r.raw_text
cleaned_txt = [(l[:int(len(l) / 2)], l[int(len(l) / 2):int(len(l) + 1)]) for l in r.raw_text]

# Part 1
def get_shared_characters(str1:str, str2:str)->str:
    chars = ''
    for c in set(str1):
        if c in str2:
            chars += c
    return chars

def get_priority(char:str)->int:
    if char.isupper():
        conv = 38
    else:
        conv = 96
    return ord(char) - conv

def get_sum_of_priorities(inp:str)->int:
    priority = 0
    for c in inp:
        priority += get_priority(c)
    return priority

priorities = [get_sum_of_priorities(c) for c in [get_shared_characters(a, b) for a, b in cleaned_txt]]
print(sum(priorities))

# Part 2
def get_sum_of_group_priorities(txt):
    group_sum = 0
    for i in range(0, len(txt), 3):
        group_sum += get_sum_of_priorities(
            get_shared_characters(
                get_shared_characters(txt[i], txt[i + 1]), 
                txt[i + 2]
            )
        )
    return group_sum

print(get_sum_of_group_priorities(txt))