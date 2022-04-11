from rich.console import Console

def render_board(board_state):
    console = Console()

    for i,row in enumerate(board_state):
        print(' ' * 30, end='')
        for j in range(len(row)):
            if board_state[i][j] == 1:
                console.print(":red_circle:", end='')
            else:
                console.print("  ", end='')
        print('')


