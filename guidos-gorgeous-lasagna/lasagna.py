"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME = 2


# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    remaining_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_time


# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(layers: int):
    """Calculate the preparation time depending on layers quantity.

    :param layers: int - quantity of layers.
    :return: int - preparation time (in minutes).

    Function that takes the amount of layers in the lasagna
    and multiplies it with PREPARATION_TIME constant`.
    """
    prep_time = layers * PREPARATION_TIME
    return prep_time


# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time spent in preparation and baking of the lasagna.

    :param number_of_layers: int - quantity of layers.
    :param elapsed_bake_time: int - baking time elapsed
    :return: int - total time spent.

    Function that takes the amount of layers in the lasagna
    and sums it with elapsed_bake_time parameter`.
    """
    preparation = preparation_time_in_minutes(number_of_layers)
    time_spent = preparation + elapsed_bake_time

    return time_spent
