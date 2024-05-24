from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    new_set=set()
    for i in dish_ingredients:
        if i not in new_set:
            new_set.add(i)
    new_format= dish_name,new_set
    return new_format



def check_drinks(drink_name, drink_ingredients):
    new_set=set()
    for i in drink_ingredients:
        new_set.add(i)
    if len(new_set.intersection(ALCOHOLS)>0):
        return drink_name.append('Cocktail')
    else:
        return drink_name.append('Mocktail')
