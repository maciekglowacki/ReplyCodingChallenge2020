import random

def count_signs(office_floor, sign):
    counter = 0
    for line in office_floor:
        for el in line:
            if el == sign:
                counter = counter+1
    return counter


def workers_positions(office_floor, sign):
    positions = []
    for y, row in enumerate(office_floor):
        for x, cell in enumerate(row):
            if office_floor[y][x] == sign:
                positions.append([y,x])
    return positions


def assign_positions(office_floor,workers, available_positions):
    positions = []
    for i, worker in enumerate(workers):
        if i < len(available_positions):
            worker.y = available_positions[i][0]
            worker.x = available_positions[i][1]
            positions.append([worker.x,worker.y])
            # print(f'X pos: {worker.x}')
            # print(f'Y pos: {worker.y}')    
        else:
            worker.y = 'X'
            worker.x = 'X'
            positions.append([worker.x,worker.y])
    return positions

def output_workers_positions(developers, managers):
    [print(f'{developer.x} {developer.y}') if developer.x != 'X' else print(f'{developer.x}') for developer in developers ]
    [print(f'{manager.x} {manager.y}') if manager.x != 'X' else print(f'{manager.x}') for manager in managers]




def sort_workers_by_company_and_bonus(workers):
    sorted_workers = sorted(workers, key = lambda worker: (worker.company, worker.bonus_potential),reverse=True)
    return sorted_workers

def solve(office_floor, developers, managers):
    available_managers_positions = workers_positions(office_floor,"M")
    available_developers_positions = workers_positions(office_floor,"_")
    developers_positions = assign_positions(office_floor,developers,available_developers_positions)
    managers_positions = assign_positions(office_floor,managers,available_managers_positions)
    # output_workers_positions(developers,managers)
    sorted_developers = sort_workers_by_company_and_bonus(developers)
    [print(f'Developer company: {developer.company}, developer bonus: {developer.bonus_potential}') for developer in sorted_developers]
