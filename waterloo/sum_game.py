days = int(input())

swifts = [int(_) for _ in input().split(" ")]
semaphores = [int(_) for _ in input().split(" ")]

k = 0

swift_sum = 0
semaphores_sum = 0

for i in range(days):
    swift_sum += swifts[i]
    semaphores_sum += semaphores[i]
    if swift_sum == semaphores_sum:
        k = i + 1

print(k)