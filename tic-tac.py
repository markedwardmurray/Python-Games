# A tic-tac-toe game by Mark Edward Murray


print "Shall we play a game?"


def new_game():
  board = [ ["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"] ]
  turn = "X"
  print_board(board)
  for counter in range(9):
    play_turn(turn, board)
    if check_for_win(turn, board) == True:
      break
    turn = switch_turns(turn)
  print "The game is over."
  ask_to_play_again()

def set_valid_moves(board):
  valid_moves = []
  for row in board:
    for tile in row:
      if tile != "X" and tile != "O":
        valid_moves.append(tile)
  return valid_moves

def print_board(board):
  for row in board:
    print " ".join(row)

def switch_turns(turn):
  if turn == "X":
    turn = "O"
  elif turn == "O":
    turn = "X"
  return turn

def get_valid_selection(turn, board):
  valid_moves = set_valid_moves(board)
  selection = raw_input("Turn: %s -- Select a tile to claim by entering 1 - 9: " % turn)
  if selection in valid_moves:
     return selection
  else:
     return get_valid_selection(turn, board)

def play_turn(turn, board):
  selection = get_valid_selection(turn, board)
  for row in board:
    if selection in row:
      index = row.index(selection)
      row[index] = turn
      break
  print_board(board)

def check_for_win(turn, board):
  victory = [turn, turn, turn]
  col1 = [ board[0][0], board[1][0], board[2][0] ]
  col2 = [ board[0][1], board[1][1], board[2][1] ]
  col3 = [ board[0][2], board[1][2], board[2][2] ]
  diag1 = [ board[0][0], board[1][1], board[2][2] ]
  diag2 = [ board[0][2], board[1][1], board[2][0] ]
  if board[0] == victory or \
     board[1] == victory or \
     board[2] == victory or \
     col1 == victory or \
     col2 == victory or \
     col3 == victory or \
     diag1 == victory or \
     diag2 == victory:
     print "%s wins the game!" % turn
     return True

def ask_to_play_again():
  answer = raw_input("Shall we play again? (y/n) ")
  if answer == "y":
    new_game()

new_game()
