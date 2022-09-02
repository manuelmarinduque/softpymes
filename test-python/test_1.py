""" 
  1) consulte la información del archivo data.py
  cree un objeto que contenga las empresas y dentro 
  las sucursales que corresponden para cada empresa
"""

from copy import deepcopy
from data import get_branches, get_companies


def companies_and_branches(companies: list[dict]):
  for company in companies:
    branches: list[int] = company.get('branches', [])
    company['branches'] = new_branches_attr(branches)
  return companies
    

def new_branches_attr(branches: list[int]):
  branches_attr: list = []
  for branch_id in branches:
    branch_name: str = get_branch_by_id(branch_id)
    branches_attr.append(branch_name)
  return branches_attr


def get_branch_by_id(branch_id_to_search: int):
  branches: list[dict] = get_branches()
  for branch in branches:
    branch_id = branch.get('id', None)
    if branch_id == branch_id_to_search:
      return branch


if __name__ == '__main__':
  companies = get_companies()
  print(companies_and_branches(deepcopy(companies)))
