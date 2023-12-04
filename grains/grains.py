def square(number):
    if number < 1 or number > 64:
        raise ValueError("Only numbers between 1 and 64.")
    board = []
    num = 1
    while len(board) < 64:
        board.append(num)
        num = num * 2  
    return board[number - 1]


def total():
    board = []
    num = 1
    while len(board) != 64:
        board.append(num)
        num = num * 2  
    return num - 1


##ANOTHER SOLUTION

def square(number: int) -> int:
    if number < 1 or number > 64:
        raise ValueError('Number not between 1 and 64!')
    return 1 << number - 1


def total() -> int:
    return (1 << 64) - 1
