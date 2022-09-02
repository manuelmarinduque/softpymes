"""
  3) ordenar los terceros que se tienen en el archivo data.py 
  por nombre, para obtener el nombre correcto se debe tener en 
  cuenta la siguiente validación:
  
  si el tercero tiene un (tradename != '') entonces se muestra este valor, 
  en caso contrario se debe obtener concatenando los siguientes 
  campos: (firstname, lastname, maidenname) en el orden dado
"""

from copy import deepcopy
from data import get_thirds


def sort_thirds_by_name(thirds: list[dict]):
  add_aux_third_name(thirds)
  return sorted(thirds, key=lambda x: x['aux_name'])

def add_aux_third_name(thirds: list[dict]):
  for third in thirds:
    tradename = third.get('tradename', None)
    if tradename:
      third['aux_name'] = tradename
    else:
      aux_name = get_third_name(third)
      third['aux_name'] = aux_name


def get_third_name(third: dict) -> str:
  firstname = third.get('firstname', None)
  lastname = third.get('lastname', None)
  maidenname = third.get('maidenname', None)
  return f'{firstname} {lastname} {maidenname}'


if __name__ == '__main__':
  thirds = get_thirds()
  print(sort_thirds_by_name(deepcopy(thirds)))
