n = int(input())

heights = [int(_) for _ in input().split(" ")]
widths = [int(_) for _ in input().split(" ")]

area = 0

for i in range(n):
    area += widths[i] * ((heights[i] + heights[i + 1]) / 2)

print(area)