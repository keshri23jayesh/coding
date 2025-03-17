# https://www.youtube.com/watch?v=3A1XJbRs_6A&list=PL-Jc9J83PIiHfqDcLZMcO9SsUDY4S3a-v&index=14
# rotten oranges is extension of this.

from queue import Queue

graph = [
    [1, 3],
    [0, 2],
    [1, 3],
    [0, 2, 4],
    [3, 5, 6],
    [4, 6],
    [5, 4],
]



infected = [0] * len(graph)
infection_queue = Queue()
infection_queue.put((6, 1))


while infection_queue.qsize():
    patient, time = infection_queue.get()
    if infected[patient] > 0:
        continue
    else:
        infected[patient] = time

    for nbr in graph[patient]:
        if infected[nbr] == 0:
            infection_queue.put((nbr, time+1))

for i,v in enumerate(infected):
    print(i, v)