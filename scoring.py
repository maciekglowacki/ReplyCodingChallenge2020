from developer import Developer
from manager import Manager
from input_parser import read_input

def get_work_potential(dev1, dev2):
  all_skills = list(set(dev1.skills + dev2.skills))
  different = [x for x in all_skills if (x not in dev1.skills) or (x not in dev2.skills)]
  common = [x for x in all_skills if x in dev1.skills and x in dev2.skills]
  return len(common) * len(different)

def get_bonus_potential(emp1, emp2):
  return emp1.bonus_potential + emp2.bonus_potential

def _get_dev_or_pm(x, y, devs_and_pms):
  return [p for p in devs_and_pms if p.x == x and p.y == y][0]

def get_score(floor, devs, pms):
  devs_and_pms = devs + pms
  result = 0
  for y in range(len(floor) - 1):
    for x in range(len(floor[y])):
      target = floor[y][x]
      right = floor[y][x + 1]
      down = floor[y + 1][x]

      p_target = _get_dev_or_pm(x, y, devs_and_pms)
      p_right = _get_dev_or_pm(x + 1, y, devs_and_pms)
      p_down = _get_dev_or_pm(x, y + 1, devs_and_pms)

      # horizontaly
      if target == '_' and right == '_':
        result += get_work_potential(p_target, p_right)
      elif target == 'M' or target == '_' and right == 'M' or right == '_':
        result += get_bonus_potential(p_target, p_right)
      # verticaly
      if target == '_' and down == '_':
        result += get_work_potential(p_target, p_down)
      elif target == 'M' or target == '_' and down == 'M' or down == '_':
        result += get_bonus_potential(p_target, p_down)
  
  return result

