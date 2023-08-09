from food import Food
import functools
from typing import List


def greedy(items, capacity: float, key_function):
    items_copy = sorted(items, key=key_function, reverse=True)
    print(items_copy)
    result = []
    total_value = 0.0

    for item in items_copy:
        if item.cost <= capacity:
            result.append(item)
            capacity -= item.cost
            total_value += item.value

    return result, total_value


def optimum_subject_to_capacity(items: List[Food], capacity: int) -> int:
    @functools.lru_cache(None)
    def optimum_subject_to_item_and_capacity(k, available_capacity):
        if k < 0:
            return 0, []

        without_curr_item_value, without_curr_item_items = optimum_subject_to_item_and_capacity(k - 1, available_capacity)

        if available_capacity < items[k].cost:
            return without_curr_item_value, without_curr_item_items

        with_curr_item_value, with_curr_item_items = optimum_subject_to_item_and_capacity(k - 1, available_capacity - items[k].cost)
        with_curr_item_value += items[k].value
        with_curr_item_items = with_curr_item_items + [items[k]]

        if with_curr_item_value > without_curr_item_value:
            return with_curr_item_value, with_curr_item_items
        else:
            return without_curr_item_value, without_curr_item_items

    return optimum_subject_to_item_and_capacity(len(items) - 1, capacity)


def test(foods, capacity):
    print('Use greedy by density to allocate', capacity, 'calories')
    print(greedy(foods, capacity, lambda food: food.density))

    print('\nUse optimum_subject_to_capacity to allocate', capacity, 'calories')
    print(optimum_subject_to_capacity(foods, capacity))


if __name__ == '__main__':
    names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
    values = [89, 90, 95, 100, 90, 79, 50, 10]
    calories = [123, 154, 258, 354, 365, 150, 95, 195]
    foods = list(map(Food, names, values, calories))

    test(foods, 750)
