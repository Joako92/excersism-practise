def add_me_with_my_friends(queue, index, person_name):
    """Insert the late arrival's name at a specific index of the queue.

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """

    queue.insert(index, person_name)
    return queue


print(add_me_with_my_friends(['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 0, 'Bucky'))
