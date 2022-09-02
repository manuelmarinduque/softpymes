"""
  5) ordenar los terceros que se tienen en el archivo data.py por nombre y 
  agregar dentro de cada tercero una propiedad que muestre la compañia a la que pertenece
"""

from copy import deepcopy
from data import get_thirds, get_companies
from test_3 import sort_thirds_by_name


def sort_by_name_adding_company(thirds: list[dict]):
  sorted_thirds = sort_thirds_by_name(thirds)
  for third in sorted_thirds:
    third_company_id = third.get('companyid', None)
    third['company_details'] = get_company_by_id(third_company_id)
  return sorted_thirds


def get_company_by_id(company_id_to_search: int):
  companies: list[dict] = get_companies()
  for company in companies:
    company_id = company.get('id', None)
    if company_id == company_id_to_search:
      return company


if __name__ == '__main__':
  thirds: list[dict] = get_thirds()
  print(sort_by_name_adding_company(deepcopy(thirds)))
