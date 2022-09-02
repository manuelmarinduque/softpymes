"""
9) realice una consulta al archivo data.py, muestre todos los items, 
  ordenelos por nombre y dentro de cada item agregue el color correspondiente,
  en caso de que esté lo tenga. 
  
  El resultado del ordenando debe ser así, en la parte inicial los items 
  que no tienen color y en la parte final los que si tienen color, todo dentro de
  un mismo objeto
"""

from copy import deepcopy
from data import get_items
from test_7 import get_sorted_items_not_color
from test_8 import get_sorted_items_with_color

if __name__ == '__main__':
  items: list[dict] = get_items()
  print(get_sorted_items_not_color(deepcopy(items)) + get_sorted_items_with_color(deepcopy(items)))