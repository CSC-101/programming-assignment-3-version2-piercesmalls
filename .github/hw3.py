import data
from build_data import CountyDemographics
from typing import List

def population_total(lst: List[CountyDemographics]) -> int:
    return sum(county.population["2014 Population"] for county in lst)