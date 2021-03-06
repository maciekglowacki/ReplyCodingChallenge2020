from manager import Manager
from developer import Developer


def read_input():
    width, height = [int(x) for x in input().split()]

    office_floor = []
    developers = []
    managers = []


    office_floor = [[x for x in input()]for y in range(height)]


    

    developers_count = input()
    developers_count = int(developers_count)

    for index in range(developers_count):
        line = input().split()
        company = line[0]
        bonus_potential = int(line[1])
        skills_count = int(line[2])
        skills = line[3:]
        developers.append(
            Developer(index, company, bonus_potential, skills_count, skills))

    managers_count = input()
    managers_count = int(managers_count)

    for index in range(managers_count):
        company, bonus_potential = input().split()
        bonus_potential = int(bonus_potential)
        managers.append(Manager(index, company, bonus_potential))

    return office_floor, developers, managers
