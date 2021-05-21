t = int(input())

for i in range(1, t+1):
    n = int(input())
    s = input()
    length = 1
    answers = ["1"]
    for j in range(1, len(s)):
        if ord(s[j]) <= ord(s[j-1]):
            length = 0
        length += 1
        answers.append(str(length))
    print(f"Case #{i}: {' '.join(answers)}")