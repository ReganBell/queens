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

def sol_string(queens):
    return str(sorted(list(queens)))

#return list of queens
def rec_search(queens, q_x, q_y, spaces):
    queens[(q_x, q_y)] = True
    spaces = [(x,y) for x,y in spaces if not attackable(q_x, q_y, x, y, N)]
    if len(spaces) == 0:
        return [sol_string(queens)] if len(queens) == N else []
    else:
        sols = []
        for s_x, s_y in spaces:
            sols += rec_search(queens.copy(), s_x, s_y, [(x,y) for x,y in spaces if not attackable(q_x, q_y, x, y, N)])
        return sols

spaces = []
for x in range(0, N):
    for y in range(0, N):
        spaces.append((x,y))
sol_set = set()
for q_x, q_y in spaces:
    for sol in rec_search({}, q_x, q_y, [(x,y) for x,y in spaces if not attackable(q_x, q_y, x, y, N)]):
        sol_set.add(sol)
print(len(sol_set))
