"""
  4) ordenar los terceros que se tienen en el archivo data.py por identificationNumber
"""

from copy import deepcopy
from data import get_thirds


def sort_by_id_num(thirds: list[dict]):
  return sorted(thirds, key=lambda x: x['identificationNumber'])


if __name__ == '__main__':
  thirds: list[dict] = get_thirds()
  print(sort_by_id_num(deepcopy(thirds)))
