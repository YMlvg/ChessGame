from chess import Board, King, Queen, Bishop, Knight, Rook, Pawn, ConsoleInterface
import curses

ui = ConsoleInterface()
game = Board(inputf=ui.get_player_input,
             printf=ui.set_msg,
             )
game.start()
while game.winner() is None:
    ui.set_board(game.display())
    while True:
        start, end = game.prompt()
        if game.valid_move(start, end):
            break
        else:
            ui.set_msg(f'Invalid move: {start} -> {end}')
    ui.set_msg(game.format_move(start, end))
    game.update(start, end)
    game.next_turn()
ui.set_msg(f'Game over. {game.winner()} player wins!')

