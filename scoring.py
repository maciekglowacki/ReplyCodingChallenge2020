from developer import Developer
from manager import Manager
from input_parser import read_input
from output_parser import read_output

def get_work_potential(dev1, dev2):
  all_skills = list(set(dev1.skills + dev2.skills))
  different = [x for x in all_skills if (x not in dev1.skills) or (x not in dev2.skills)]
  common = [x for x in all_skills if x in dev1.skills and x in dev2.skills]
  return len(common) * len(different)

def get_bonus_potential(emp1, emp2):
  if (emp1.company == emp2.company):
    return emp1.bonus_potential * emp2.bonus_potential
  return 0

def _get_dev_or_pm(x, y, devs_and_pms):
  f = [p for p in devs_and_pms if p.x == x and p.y == y]
  return f[0] if f else None

def _get_adjacent_score(e1, e2, emp1, emp2):
  result = 0
  if e1 == '_' and e2 == '_':
    score = get_work_potential(emp1, emp2) + get_bonus_potential(emp1, emp2)
    result += score
  elif e1 == 'M' or e1 == '_' and e2 == 'M' or e2 == '_':
    score = get_bonus_potential(emp1, emp2)
    result += score
  return result

def get_score(floor, devs, pms):
  devs_and_pms = devs + pms
  result = 0
  # verticaly
  for y in range(len(floor) - 1):
    for x in range(len(floor[y])):
      target = floor[y][x]
      next = floor[y + 1][x]

      p_target = _get_dev_or_pm(x, y, devs_and_pms)
      p_next = _get_dev_or_pm(x, y + 1, devs_and_pms)

      if not (p_target and p_next):
        continue

      result += _get_adjacent_score(target, next, p_target, p_next)

  # horizontaly
  for y in range(len(floor)):
    for x in range(len(floor[y]) - 1):
      target = floor[y][x]
      next = floor[y][x + 1]

      p_target = _get_dev_or_pm(x, y, devs_and_pms)
      p_next = _get_dev_or_pm(x + 1, y, devs_and_pms)

      if not (p_target and p_next):
        continue

      result += _get_adjacent_score(target, next, p_target, p_next)
  
  return result

if __name__ == '__main__':
  office_floor, developers, managers = read_input()
  developers_pos, managers_pos = read_output(len(developers), len(managers))
  for dev in developers:
    for poses in developers_pos:
      if dev.id == poses[0]:
        dev.x = poses[1]
        dev.y = poses[2]
  
  for pm in managers:
    for poses in managers_pos:
      if pm.id == poses[0]:
        pm.x = poses[1]
        pm.y = poses[2]
  
  score = get_score(office_floor, developers, managers)
  print(score)
