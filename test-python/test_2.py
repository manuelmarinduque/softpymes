"""
  2) teniendo en cuenta el punto 1, cree una función que permita
  consultar las sucursales por su id, debe hacerse el mismo procedimiento
  que se realizó en el punto 1, pero, utilizando la función creada
"""

from data import get_branches
from test_1 import get_branch_by_id


if __name__ == '__main__':
  branches: list[dict] = get_branches()
  for i in range(len(branches)+1):
    print(get_branch_by_id(i))
