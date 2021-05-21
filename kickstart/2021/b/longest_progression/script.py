t = int(input())

for i in range(1, t+1):
    n = int(input())
    a = [int(_) for _ in input().split(" ")]
    common_differences = []
    for j in range(1, len(a)):
        common_differences.append(a[j] - a[j-1])
    print(common_differences)
    print(f"Case #{i}: ")
