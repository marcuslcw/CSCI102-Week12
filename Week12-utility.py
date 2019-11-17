def PrintOutput(string_input):
    print('OUTPUT %s' % string_input)

def LoadFile(file):
    file_list = []
    with open(file, 'r') as o_file:
        for line in o_file:
            line = line.strip()
            file_list.append(line)
    return file_list

def UpdateString(string_1, string_2, index_int):
    i = 0
    new_string = ''
    for i in range(len(string_1)):
        if i == index_int:
            new_string += string_2
        else:
            new_string += string_1[i]    
    return new_string

def FindWordCount(a_list, a_string):
    count = 0
    for word in a_list:
        count += word.count(a_string)
    return count

def ScoreFinder(list_1, list_2, string_3):
    c_string_3 = string_3.capitalize()
    for player in list_1:
        if player != c_string_3 and list_1.index(player) != len(list_1) - 1:
            continue
        elif player == c_string_3:
            score = list_2[list_1.index(player)]
            print('OUTPUT: %s got a score of %s' %(player, score))
            break
        else:
            print('OUTPUT: player not found')
