from chess import Board, King, Queen, Bishop, Knight, Rook, Pawn, ConsoleInterface,TextInterface
import curses
ui = TextInterface()
game = Board(inputf=ui.get_player_input,
             printf=ui.set_msg,
             )
game.start()
while game.winner is None:
    # import pdb; pdb.set_trace()
    ui.set_board(game.display())
    print(ui.inputstr_list)
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

