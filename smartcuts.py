from collections import deque

def attackable(q_x, q_y, x, y, N):
    if q_x == x:
        return True
    if q_y == y:
        return True
    for k in range(-N, N):
        if x+k == q_x and y+k == q_y:
            return True
        if x-k == q_x and y+k == q_y:
            return True
    return False
    
N = 5

def rec_search(queens, q_x, q_y, spaces):
    spaces = [(x,y) for x,y in spaces if not attackable(q_x, q_y, x, y, N)]
    sols = []
    for i in range(len(spaces)):
        queens_i = queens.copy()
        x_i, y_i = spaces[i]
        queens_i[(x_i, y_i)] = True
        sols.append(rec_search(queens_i, x_i, y_i, spaces[0:i] + spaces[i:len(spaces)]))
    return sols

def starting_with(x_0, y_0):
    queens = {}
    spaces = []
    for x in range(0, N):
        for y in range(0, N):
            spaces.append((x,y))
    q_x, q_y = x_0, y_0
    queens[(q_x, q_y)] = True
    while len(spaces):
        spaces = [(x,y) for x,y in spaces if not attackable(q_x, q_y, x, y, N)]
        solutions = []
        for i in range(len(spaces)):
            queens_i = queens.copy()
            x_i, y_i = spaces[i]
            queens_i[(x_i, y_i)] = True
            solutions.append(rec_search(queens_i, x_i, y_i, spaces[0:i] + spaces[i:len(spaces)]))
        if len(spaces):
            q_x, q_y = spaces.pop()
            queens[(q_x,q_y)] = True
    return solutions
    # return sorted([str(a) + str(b) for a,b in list(queens)])

solutions = set()
for x in range(0, N):
    for y in range(0, N):
        sol = starting_with(x,y)
        if len(sol) == N:
            solutions.add(''.join(sol))
            print(len(sol))
        else:
            print(len(sol))
print(solutions)
print(len(solutions))
        # queens = {}
        # start = (x,y)
        # deque.appendleft(start)
        # while len(deque):
        #     q_x, q_y = deque.pop()
        #     queens[(q_x,q_y)] = True
        #     for space in deque:

        #     for x in range(0, N):
        #         for y in range(0, N):
        #             if x != q_x and y != q_y and diagonal(x, y):
        #                 deque.appendleft((x,y))




