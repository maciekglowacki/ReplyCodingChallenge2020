from input_parser import read_input


def count_signs(office_floor, sign):
    counter = 0
    for line in office_floor:
        for el in line:
            if el == sign:
                counter = counter+1
    return counter


if __name__ == '__main__':
    office_floor, developers, managers = read_input()
    workers = len(developers) + len(managers)
    work_places = count_signs(office_floor,"_") + count_signs(office_floor,"M")
    #x and y is swapped
    print(office_floor[2][1])
    print(f'Workers count: {workers}')
    print(f'Workplaces: {work_places}')


