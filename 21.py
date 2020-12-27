import re
from functools import reduce

example_input = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

with open('inputs/21.txt') as f:
    myinput = f.read()


def parse_line(line):
    parse_regex = re.compile(r'((\w+ )+)\(contains ((\w+, )*\w+)\)')
    matches = parse_regex.match(line)
    ingredients = set(matches.group(1).strip().split(' '))
    allergens = matches.group(3).replace(' ', '').split(',')

    return (ingredients, allergens)


def find_possible_allergens(allergen_map):
    return reduce(lambda acc, x: acc | x, allergen_map.values(), set())


def affinate_allergens(allergen_map):
    def clean_allergens(to_remove, allergen_map):
        for allergen, ingredients in allergen_map.items():
            if len(ingredients) > 1:
                allergen_map[allergen] -= to_remove
            if len(ingredients) == 1:
                to_remove = to_remove.union(ingredients)
        return to_remove

    to_remove = set()
    possible_allergens = find_possible_allergens(allergen_map)

    while to_remove != possible_allergens:
        to_remove = clean_allergens(to_remove, allergen_map)

    clean_allergens(to_remove, allergen_map)


def part1(data):
    allergen_map = {}
    ingredients_count = {}
    for line in data.split('\n'):
        ingredients, allergens = parse_line(line)
        for allergen in allergens:
            if allergen in allergen_map:
                allergen_map[allergen] &= ingredients
            else:
                allergen_map[allergen] = ingredients.copy()
        for ingredient in ingredients:
            if ingredient in ingredients_count:
                ingredients_count[ingredient] += 1
            else:
                ingredients_count[ingredient] = 1

    possible_allergens = reduce(
        lambda acc, x: acc | x, allergen_map.values(), set())

    all_ingredients = set(ingredients_count.keys())
    non_allergens = all_ingredients - possible_allergens

    affinate_allergens(allergen_map)

    print(f'part 1: {sum([ingredients_count[x] for x in non_allergens])}')
    allergens_sorted = sorted(allergen_map.keys())

    print(
        f'part 2: {",".join(["".join(allergen_map[x]) for x in allergens_sorted])}')


part1(myinput)
