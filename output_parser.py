def read_output(developers_count, managers_count):
    developers = []
    managers = []

    for developer in range(developers_count):
        line = input().split()
        if (line[0] != 'X'):
          developers.append((developer, int(line[0]), int(line[1])))
    
    for manager in range(managers_count):
        line =  input().split()
        if (line[0] != 'X'):
          managers.append((manager, int(line[0]), int(line[1])))
    
    return (developers, managers)

if __name__ == '__main__':
    developers, managers = read_output(10, 3)
    print(developers)
    print(managers)
