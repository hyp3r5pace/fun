from board import random_state
from render import render_board
from next_state import cell_next_status, board_next_state

def main():
    board_state = random_state(10,10)
    while True:
      render_board(board_state)
      board_state = board_next_state(board_state)
      print('\n')

if __name__ == "__main__":
    main()
