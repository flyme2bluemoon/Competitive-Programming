n = int(input())

for _ in range(n):
    uncompress = input()
    compress = []
    
    current_char = uncompress[0]
    current_char_counter = 0
    for i in uncompress:
        if i != current_char:
            print(f"{current_char_counter} {current_char}", end=" ")
            current_char = i
            current_char_counter = 0
        current_char_counter += 1
    print(f"{current_char_counter} {current_char}")
