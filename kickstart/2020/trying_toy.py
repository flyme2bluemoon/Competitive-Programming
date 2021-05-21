from queue import PriorityQueue

T = int(input())

for t in range (1, T + 1):
    the_number_of_toys = int(input())
    the_toys = []
    the_enjoyment_values = []
    the_remembrance_values = []
    the_sum_values = []

    for i in range(the_number_of_toys):
        the_toys.append([int(s) for s in input().split(" ")])
        the_enjoyment_values.append(the_toys[i][0])
        the_remembrance_values.append(the_toys[i][1])
        the_sum_values.append(the_toys[i][0] + the_toys[i][1])

    the_sum_of_enjoyment_time = sum(the_enjoyment_values)

    the_max_time = the_sum_of_enjoyment_time
    the_min_removed = 0

    the_time = the_sum_of_enjoyment_time # cur_time
    the_removed = 0

    try:
        the_toy_pqueue = PriorityQueue()

        for i in range(len(the_sum_values)):
            the_toy_pqueue.put((-the_sum_values[i], i))
            the_time += the_enjoyment_values[i]

            while not the_toy_pqueue.empty():
                the_top_of_pqueue = list(the_toy_pqueue.get()) # the_sum_and_index
                the_top_of_pqueue[0] *= -1
                if the_top_of_pqueue[0] > the_sum_of_enjoyment_time:
                    the_time -= (the_enjoyment_values[the_top_of_pqueue[1]] * 2)
                    the_sum_of_enjoyment_time -= the_enjoyment_values[the_top_of_pqueue[1]]
                    the_removed += 1
                else:
                    the_top_of_pqueue[0] *= -1
                    the_toy_pqueue.put(tuple(the_top_of_pqueue))
                    break

            if the_time > the_max_time:
                the_max_time = the_time
                the_min_removed = the_removed
            elif the_time == the_max_time:
                the_min_removed = min(the_removed, the_min_removed)
    except:
        print("Failed in test case", t)

    if not the_toy_pqueue.empty():
        print(f"Case #{t}: TODO {the_removed} INDEFINITELY")
    else:
        print(f"Case #{t}: TODO {the_min_removed} {the_max_time}")