from input_parser import read_input
from solver import solve, count_signs
from random import shuffle
from scoring import get_score
from sys import argv


def output_workers_positions(workers, file_name):
  f = open(f"outputs/{file_name}","w+")
  [f.write(f'{worker[0]} {worker[1]}\n') if worker[0] != 'X' else f.write('X\n') for worker in workers]
  f.close()


if __name__ == '__main__':
  office_floor, developers, managers = read_input()
  workers = len(developers) + len(managers)
  work_places = count_signs(office_floor,"_") + count_signs(office_floor,"M")
  #x and y is swapped
  # print(office_floor[2][1])
  # print(f'Workers count: {workers}')
  # print(f'Workplaces: {work_places}')
  max_score = 0
  best_out = None
  for i in range(int(argv[-2])):
    shuffle(developers)
    shuffle(managers)
    devs_pos, mans_pos, devs, mans = solve(office_floor, developers, managers)
    # shuffle(devs_pos)
    # shuffle(mans_pos)
    # output_workers_positions(devs_pos, mans_pos)
    score = get_score(office_floor, devs, mans)
    print(score)
    if score > max_score:
      max_score = score
      best_out = devs_pos + mans_pos
      output_workers_positions(best_out, str(score) + argv[-1])
  
  print(max_score)
