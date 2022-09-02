"""
  10) realice una consulta al archivo data.py, muestre todos los terceros, reduzca la 
  información y solo muestre el nombre y la identificación, 
  ordenelos por identificación
"""

from copy import deepcopy
from data import get_thirds
from test_3 import get_third_name


def show_min_third_info(thirds: list[dict]):
  new_thirds = []
  for third in thirds:
    if tradename:= third.get('tradename', None):
      name = tradename
    else:
      name = get_third_name(third)
    new_third = {'name': name, 'identification': third.get('identificationNumber', None)}
    new_thirds.append(new_third)
  return sorted(new_thirds, key=lambda x: x['identification'])


if __name__ == '__main__':
  thirds: list[dict] = get_thirds()
  print(show_min_third_info(deepcopy(thirds)))
