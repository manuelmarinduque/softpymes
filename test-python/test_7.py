"""
  7) realice una consulta al archivo data.py, muestre los items que no tienen colores 
  y ordenelos por nombre
"""


from copy import deepcopy
from data import get_items


def get_sorted_items_not_color(items: list[dict]):
  items_not_color = get_items_by_not_color(items)
  return sorted(items_not_color, key=lambda x: x['name'])


def get_items_by_not_color(items: list[dict]) -> list[dict]:
  items_not_color = []
  for item in items:
    item_color = item.get('color', None)
    if item_color is None:
      items_not_color.append(item) 
  return items_not_color


if __name__ == '__main__':
  items = get_items()
  print(get_sorted_items_not_color(deepcopy(items)))
