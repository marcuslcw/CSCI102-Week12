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
