import chess

def print_board(board):
    print(board)

def get_move():
    print("Enter your move in UCI format (e.g., 'e2e4' to move a piece from e2 to e4):")
    uci_move = input()
    return uci_move

def main():
    board = chess.Board()

    while not board.is_game_over():
        print_board(board)
        uci_move = get_move()

        if chess.Move.from_uci(uci_move) in board.legal_moves:
            board.push_uci(uci_move)
        else:
            print("Illegal move. Try again.")

    print("Game over. Result: ", board.result())

if __name__ == "__main__":
    main()