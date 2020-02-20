#!/usr/bin/python

import math

"""
def recipe_batches(recipe, ingredients):
  
  max_combo = 0
  for ingredient in recipe.keys():
    if recipe[ingredient] > ingredients[ingredient]:
      return 0
    elif ingredients[ingredient] // recipe[ingredient] <= 0:
      max_combo = ingredients[ingredient] // recipe[ingredient]
  
  return max_combo
"""

def recipe_batches(recipe, ingredients):
  max_combo = []
  if len(recipe) > len(ingredients):
    return 0 
  for  key in recipe:
    if key not in ingredients:
      return 0 
    else:
      max_combo.append(ingredients[key] // recipe[key])
  return min(max_combo)
      
  












if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))