N = int(input())
q = list(map(int, input().split()))

people = [x for x in range(1, 1+N)]
queue = []
for idx, person in enumerate(people):
    queue.insert(len(queue)-q[idx], person)
    
print(' '.join(map(str, queue)))