from data import CountyDemographics
from typing import List

# Part 1
def population_total(counties: List['CountyDemographics']) -> int:
   return sum(county.population['2014 Population'] for county in counties)
# Part 2
def filter_by_state(counties: List['CountyDemographics'], state_abbr: str) -> List['CountyDemographics']:
   return [county for county in counties if county.state == state_abbr]
# Part 3
def population_by_education(counties: List['CountyDemographics'], key: str) -> float:
   return sum((county.education.get(key, 0) / 100) * county.population['2014 Population'] for county in counties)
def population_by_ethnicity(counties: List['CountyDemographics'], key: str) -> float:
   return sum((county.ethnicities.get(key, 0) / 100) * county.population['2014 Population'] for county in counties)
def population_below_poverty_level(counties: List['CountyDemographics']) -> float:
   return sum((county.income['Persons Below Poverty Level'] / 100) * county.population['2014 Population'] for county in counties)
# Part 4
def percent_by_education(counties: List['CountyDemographics'], key: str) -> float:
   total_population = population_total(counties)
   sub_population = population_by_education(counties, key)
   return (sub_population / total_population * 100) if total_population else 0
def percent_by_ethnicity(counties: List['CountyDemographics'], key: str) -> float:
   total_population = population_total(counties)
   sub_population = population_by_ethnicity(counties, key)
   return (sub_population / total_population * 100) if total_population else 0
def percent_below_poverty_level(counties: List['CountyDemographics']) -> float:
   total_population = population_total(counties)
   sub_population = population_below_poverty_level(counties)
   return (sub_population / total_population * 100) if total_population else 0
# Part 5
def education_greater_than(counties: List['CountyDemographics'], key: str, threshold: float) -> List['CountyDemographics']:
   return [county for county in counties if county.education.get(key, 0) > threshold]
def education_less_than(counties: List['CountyDemographics'], key: str, threshold: float) -> List['CountyDemographics']:
   return [county for county in counties if county.education.get(key, 0) < threshold]
def ethnicity_greater_than(counties: List['CountyDemographics'], key: str, threshold: float) -> List['CountyDemographics']:
   return [county for county in counties if county.ethnicities.get(key, 0) > threshold]
def ethnicity_less_than(counties: List['CountyDemographics'], key: str, threshold: float) -> List['CountyDemographics']:
   return [county for county in counties if county.ethnicities.get(key, 0) < threshold]
def below_poverty_level_greater_than(counties: List['CountyDemographics'], threshold: float) -> List['CountyDemographics']:
   return [county for county in counties if county.income['Persons Below Poverty Level'] > threshold]
def below_poverty_level_less_than(counties: List['CountyDemographics'], threshold: float) -> List['CountyDemographics']:
   return [county for county in counties if county.income['Persons Below Poverty Level'] < threshold]
