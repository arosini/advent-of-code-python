from util.Util import timeit


class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)


def get_best_recipe(current_recipe, current_idx, ingredient_count, calorie_count, ingredients):
    currently_used = sum(current_recipe)

    if current_idx == len(current_recipe) - 1:
        current_recipe[current_idx] = ingredient_count - currently_used

        if calorie_count is not None:
            calories = sum(current_recipe[i] * ingredients[i].calories for i in range(len(ingredients)))
            if calories != calorie_count: return None

        return get_recipe_value(current_recipe, ingredients)

    best_result = 0
    for i in range(ingredient_count + 1 - currently_used):
        current_recipe[current_idx] = i
        result = get_best_recipe(current_recipe.copy(), current_idx + 1, ingredient_count, calorie_count, ingredients)
        if result is not None and result > best_result: best_result = result

    return best_result


def get_recipe_value(recipe, ingredients):
    capacity = max(0, sum(recipe[i] * ingredients[i].capacity for i in range(len(ingredients))))
    durability = max(0, sum(recipe[i] * ingredients[i].durability for i in range(len(ingredients))))
    flavor = max(0, sum(recipe[i] * ingredients[i].flavor for i in range(len(ingredients))))
    texture = max(0, sum(recipe[i] * ingredients[i].texture for i in range(len(ingredients))))

    return capacity * durability * flavor * texture


@timeit
def part1():
    ingredients = list()
    with open("input/Day15.txt") as file:
        lines = file.readlines()
        for line in lines:
            name, properties_raw = line.strip().split(":")
            properties = properties_raw.strip().replace(",", "").split()
            ingredients.append(Ingredient(name, int(properties[1]), int(properties[3]), int(properties[5]),
                                          int(properties[7]), int(properties[9])))

    print(get_best_recipe([0] * len(ingredients), 0, 100, None, ingredients))


@timeit
def part2():
    ingredients = list()
    with open("input/Day15.txt") as file:
        lines = file.readlines()
        for line in lines:
            name, properties_raw = line.strip().split(":")
            properties = properties_raw.strip().replace(",", "").split()
            ingredients.append(Ingredient(name, int(properties[1]), int(properties[3]), int(properties[5]),
                                          int(properties[7]), int(properties[9])))

    print(get_best_recipe([0] * len(ingredients), 0, 100, 500, ingredients))


part1()
print()
part2()

