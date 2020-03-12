from input_parser import read_input
from solver import solve, count_signs




if __name__ == '__main__':
    office_floor, developers, managers = read_input()
    workers = len(developers) + len(managers)
    work_places = count_signs(office_floor,"_") + count_signs(office_floor,"M")
    #x and y is swapped
    # print(office_floor[2][1])
    # print(f'Workers count: {workers}')
    # print(f'Workplaces: {work_places}')
    solve(office_floor, developers, managers)
        
