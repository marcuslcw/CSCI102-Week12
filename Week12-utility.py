def PrintOutput(string_input):
    print('OUTPUT %s' % string_input)

def LoadFile(file):
    file_list = []
    with open(file, 'r') as o_file:
        for line in o_file:
            line = line.strip()
            file_list.append(line)
    return file_list
