import parse
from typing import List

inp = parse.get_input(False)
text = inp.raw_text

tst = [
    '30373',
    '25512',
    '65332',
    '33549',
    '35390',
]

# Part 1
def is_visible(i:int, j:int, char:int, txt:List[str])->bool:
    row_before = all(num < char for num in set([int(c) for c in txt[i][:j]]))
    row_after = all(num < char for num in set([int(c) for c in txt[i][j + 1:]]))
    col_before = all(num < char for num in set(([int(c[j]) for c in [line for line in txt[:i]]])))
    col_after = all(num < char for num in set([int(c[j]) for c in [line for line in txt[i + 1:]]]))
    if row_before or row_after or col_before or col_after:
        return True
    else:
        return False
# Part 2
def get_scenic_score_sum(txt:List[int])->int:
    if 0 in txt:
        score = txt.index(0) + 1
    else:
        score = len(txt)
    return score

def get_scenic_score(i:int, j:int, char:int, txt:List[str])->int:
    row_before_ls = [1 if int(c) < char else 0 for c in reversed(txt[i][:j])]
    row_after_ls = [1 if int(c) < char else 0  for c in txt[i][j + 1:]]
    col_before_ls = [1 if int(c[j]) < char else 0  for c in reversed([line for line in txt[:i]])]
    col_after_ls = [1 if int(c[j]) < char else 0  for c in [line for line in txt[i + 1:]]]

    row_before = get_scenic_score_sum(row_before_ls)
    row_after = get_scenic_score_sum(row_after_ls)
    col_before = get_scenic_score_sum(col_before_ls)
    col_after = get_scenic_score_sum(col_after_ls)
    return row_before * row_after * col_before * col_after

def get_tree_count(txt:List[str])->List[int]:
    visible_cnt = (len(txt) + (len(txt[0]) - 2)) * 2
    scenic_score = [[0] * len(txt[0]) for i in range(0, len(txt))]
    for i in range(1, len(txt) - 1):
        line = txt[i]
        for j in range(1, len(line) - 1):
            visible_cnt += is_visible(i, j, int(txt[i][j]), txt)
            scenic_score[i][j] = get_scenic_score(i, j, int(txt[i][j]), txt)
    return visible_cnt, max(map(max, scenic_score))

print(get_tree_count(text))