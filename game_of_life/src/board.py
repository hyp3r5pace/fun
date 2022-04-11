import random

def random_state(width, height):
    """
        Creates a randomly initialized board of size width * height
    """
    board = [[0 for i in range(width)] for j in range(height)]

    for i,row in enumerate(board):
        for j in range(len(row)):
            random_num = random.random()
            if random_num >= 0.5:
                board[i][j] = 1

    return board


if __name__ == "__main__":
    random_state(2,4)
