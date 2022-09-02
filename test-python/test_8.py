"""
  8) realice una consulta al archivo data.py, muestre los items que si tienen colores, 
  ordenelos por nombre y dentro de cada item agregue el color correspondiente
"""

from copy import deepcopy
from data import get_items, get_colors


def get_sorted_items_with_color(items: list[dict]):
  items_with_color = get_items_by_color(items)
  sorted_items = sorted(items_with_color, key=lambda x: x['name'])
  for item in sorted_items:
    color_code = item.get('color', None)
    item['color'] = get_color_by_code(color_code)
  return sorted_items


def get_color_by_code(color_code_to_search: int):
  colors: list[dict] = get_colors()
  for color in colors:
    color_code = color.get('colorCode', None)
    if color_code == color_code_to_search:
      return color


def get_items_by_color(items: list[dict]) -> list[dict]:
  items_not_color = []
  for item in items:
    item_color = item.get('color', None)
    if item_color:
      items_not_color.append(item) 
  return items_not_color


if __name__ == '__main__':
  items: list[dict] = get_items()
  print(get_sorted_items_with_color(deepcopy(items)))
