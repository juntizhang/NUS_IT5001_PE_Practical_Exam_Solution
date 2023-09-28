## Part 1 Name Similarity Degree (10 + 10 + 10 = 30 marks)
### Task 1 Iterative Name Similarity Degree (10 marks)
def common_char_i(name1,name2):
    l = min(len(name1), len(name2))
    count = 0
    for i in range(l): 
        if name1.lower()[i] == name2.lower()[i]:
            count += 1
    return count
print(common_char_i('McDonald','Andrey'))


### Task 2 Recursive Name Similarity Degree (10 marks)
def common_char_r(name1,name2):
    if not (name1 and name2):
        return 0
    else:
        if name1.lower()[0] == name2.lower()[0]:
            return 1 + common_char_r(name1[1:],name2[1:])
        else:
            return common_char_r(name1[1:],name2[1:])
print(common_char_r('Brandy','Flank'))


### Task 3 One-liner Name Similarity Degree (10 marks)
'''List comprehension approach'''
def common_char_u(name1,name2):
    return len([1 for i in list(zip(name1.lower(),name2.lower())) if i[0] == i[1]])

'''Filter approach'''
print(common_char_u('McDonald','Andrey'))

# Part 2 Text Compression (20 marks）
def text_compression(text):
    txt_lst = text.split()
    low_lst = text.lower().split()
    for ind, ele in enumerate(low_lst):
        if len(ele)>1:
            index_lst = []
            for i in range(ind+1, len(low_lst)):
                if low_lst[i] == ele:
                    index_lst.append(i)
                    low_lst[i] = '_'
            for i in index_lst:
                txt_lst[i] = str(ind + 1)
    return ' '.join(txt_lst)

text3 = 'Do you wish me a good morning or mean that it is a good morning whether I want not or that you feel good this morning or that it is morning to be good on'
print(text_compression(text3))    
text7 = 'Text compression will save the world from inefficiency Inefficiency is a blight on the world and its humanity'
print(text_compression(text7))    

# Part 3 ASCII Picture Pattern Matching (20 marks)
pic = [[' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' '], [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' '], [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' '], [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' '], [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' '], [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' '], [' ', '#', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' '], [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' '], [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' '], [' ', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#', ' ', ' '], [' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' '], [' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' '], [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ']]
pic1 = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '#', '.', '#', '.', '.', '.', '.', '.'], ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.'], ['.', '.', '#', '.', '#', '.', '#', '.', '.', '.'], ['.', '.', '.', '.', '.', '#', '.', '.', '.', '.'], ['.', '.', '.', '.', '#', '.', '#', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
part1 = ['#.#','.#.','#.#']

def pattern_matching(picture, part):
    res = []
    rows_pic, cols_pic = len(picture), len(picture[0])
    rows_part, cols_part = len(part), len(part[0])

    for i in range(rows_pic - rows_part + 1):
        for j in range(cols_pic - cols_part + 1):
            if all(picture[i + x][j + y] == part[x][y] for x in range(rows_part) for y in range(cols_part)):
                res.append((i, j, i + rows_part - 1, j + cols_part - 1))
    return res
print(pattern_matching(pic1,part1))


# Part 4 War Strategy Prediction (30 marks)
def strategic_count(mapfile):
    file = open(mapfile, "r")
    routes = file.readlines()
    file.close()

    routes_ls = [i.strip().split(" ") for i in routes]
    del routes

    location_info = dict()

    location_index = 0
    for route in routes_ls:
        location_info[route[0]] = [location_index, -1]
        location_index += 1

    return dp_retrieve_next("CountryA", location_info, routes_ls)


def dp_retrieve_next(start_location, location_info_map, routes_ls):
    if start_location == "capitalB":
        return 1
    elif start_location == "deadend":
        return 0

    location_info = location_info_map[start_location]
    location_index = location_info[0]
    location_next_possibilities = location_info[1]

    if location_next_possibilities != -1:
        return location_next_possibilities
    else:
        location_possibilities = 0
        for i in range(1, len(routes_ls[location_index])):
            next_location_possibilities = dp_retrieve_next(routes_ls[location_index][i],
                                                           location_info_map, routes_ls)
            location_possibilities += next_location_possibilities
        location_info_map[start_location][1] = max(0, location_possibilities)
        return location_possibilities

strategic_count("mapfile2.txt")