from manager import Manager
from developer import Developer

width, height = [int(x) for x in input().split()]

office_floor = []

for _ in range(height):
    line = input()
    office_floor.append(line)

# print(office_floor)

developers_count = input()
developers_count = int(developers_count)

developers = []
managers = []

for developer in range(developers_count):
    line = input().split()
    company = line[0]
    bonus_potential = line[1]
    skills_count = line[2]
    skills = line[2:]
    developers.append(Developer(company,bonus_potential,skills_count,skills))

managers_count = input()
managers_count = int(managers_count)

for manager in range(managers_count):
    company, bonus_potential = input().split()
    bonus_potential = int(bonus_potential)
    print(company)
    print(bonus_potential)
    managers.append(Manager(company,bonus_potential))

print(managers[0])