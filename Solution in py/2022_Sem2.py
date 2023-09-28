# Part 1 Plinko (10 + 10 + 10 = 30 marks) 
## Task 1 Plinko Iterative Version
def plinko_i(seq,b,m,s):
    i = 0
    res = 0
    while all([b,m,s]) and (i <=len(seq)-1 ):
        if seq[i] == 0:
            b -= 1
        elif seq[i] == 1:
            m -= 1
        else:
            s -= 1
        i += 1
        res += 1
    return res
print(plinko_i((0,1,2,0),3,3,2))

## Task 2 Plinko Recursive Version
def plinko_r(seq,b,m,s):
    if not (b and m and s and seq): return 0
    elif seq[0] == 0:
        return 1+plinko_r(seq[1:],b-1,m,s)
    elif seq[0] == 1:
        return 1+plinko_r(seq[1:],b,m-1,s)
    elif seq[0] == 2:
        return 1+plinko_r(seq[1:],b,m,s-1)

print(plinko_r((0,0,0,0,1,0,1,2),6,2,2))

## Task 3 Plinko General Version 
def plinko_general(seq,prizes):
    prize_lst = list(prizes)
    i = 0
    res = 0
    while all(prize_lst) and (i <=len(seq)-1 ):
        ind = seq[i]
        prize_lst[ind] -= 1
        i += 1
        res += 1
    return res
        
print(plinko_general((0,1,2,0,1,2,0,1,2,2,2,1,1,0,1),(4,3,4)))


## Part 2 Archaeologist Text Fragment Matching (20 + 10 marks) 
def fragment(filename,word):
    with open (filename) as f:
        data = f.read().split()
    start_lst = []
    end_lst = []
    s = ''
    for i in range(len(word)-1):
        start_lst.append(s+word[i])
        end_lst.append(word[i+1:]) 
        s = s+word[i]
    collection =  list(zip(start_lst,end_lst))
    res = collection.copy()
    for i in collection:
        if not ((i[0] in data) and (i[1] in data)):
            res.remove(i)
    return res

print(fragment('fragment_all2.txt','board'))


## Part 3 Island Perimeter (20 + 20 marks) 
map0 = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0],[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
map1 = [[0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
def count_sides(map_mat,row,col):
    up,low,left,right = 0,0,0,0
    if row == 0: up = 1
    if row == len(map_mat)-1: low = 1
    if col == 0: left = 1
    if col == len(map_mat[0])-1: right = 1

    if not up:
        if map_mat[row-1][col] == 0: up = 1
    if not low:
        if map_mat[row+1][col] == 0: low = 1
    if not left:
        if map_mat[row][col-1] == 0: left = 1
    if not right:
        if map_mat[row][col+1] == 0: right = 1
    return up+low+left+right

def total_perimeter(mp):    
    count_lst = [count_sides(mp,i,j) for i in range(len(mp)) for j in range(len(mp[i])) if mp[i][j] == 1]
    return sum(count_lst)

total_perimeter(map1)

def find_islands(matrix):
    if not matrix: return []
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def search_adjacent(r, c, current_island):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or matrix[r][c] == 0:
            return
        visited[r][c] = True
        current_island.append((r, c))
        search_adjacent(r-1, c, current_island)
        search_adjacent(r+1, c, current_island)
        search_adjacent(r, c-1, current_island)
        search_adjacent(r, c+1, current_island)

    islands = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and not visited[r][c]:
                current_island = []
                search_adjacent(r, c, current_island)
                islands.append(current_island)
    return islands

def max_island_perimeter(mp):
    islands = find_islands(mp)
    perimeter = []
    for i in islands:
        count = 0
        for j in i:
            count += count_sides(mp,j[0],j[1])
        perimeter.append(count)
    return max(perimeter)

max_island_perimeter(map1)