import random


def get_sample(iterable, number_of_items):

    if len(iterable) < number_of_items:
        number_of_items = len(iterable)

    the_sample = random.sample(iterable, number_of_items)

    return the_sample
