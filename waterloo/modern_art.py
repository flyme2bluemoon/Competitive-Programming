m = int(input()) # rows
n = int(input()) # columns

k = int(input())

row_actions = {}
column_actions = {}

for i in range(k):
    row_or_column, id_num = [_ for _ in input().split(" ")]
    id_num = int(id_num)
    if row_or_column == "R":
        if id_num in row_actions:
            row_actions[id_num] += 1
        else:
            row_actions[id_num] = 1
    else:
        if id_num in column_actions:
            column_actions[id_num] += 1
        else:
            column_actions[id_num] = 1

gold_rows = 0
gold_columns = 0

for i in row_actions:
    if row_actions[i] % 2 == 1:
        gold_rows += 1

for i in column_actions:
    if column_actions[i] % 2 == 1:
        gold_columns += 1

gold = (gold_rows * n) + (gold_columns * m) - (2 * gold_rows * gold_columns)

print(gold)