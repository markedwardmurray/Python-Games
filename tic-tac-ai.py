# A tic-tac-toe game by Mark Edward Murray
#
# One player version with AI


def ask_to_play(human):
  answer = raw_input("Shall we play a game? (y/n) ")
  ai = ""
  if human == "X":
    human = "O"
    ai = "X"
  elif human == "O":
    human = "X"
    ai = "O"
  if answer == "y":
    new_game(human, ai)

def new_game(human, ai):
  board = [ ["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"] ]
  turn = "X"
  print_board(board)
  for counter in range(9):
    if turn == human:
      play_turn(turn, board)
    elif turn == ai:
      ai_turn(turn, board)
    if check_for_win(turn, board) == True:
      break
    turn = switch_turns(turn)
  print "The game is over."
  ask_to_play(human)

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

def set_valid_moves(board):
  valid_moves = []
  for row in board:
    for tile in row:
      if tile != "X" and tile != "O":
        valid_moves.append(tile)
  return valid_moves

def play_turn(turn, board):
  selection = get_valid_selection(turn, board)
  for row in board:
    if selection in row:
      index = row.index(selection)
      row[index] = turn
      break
  print_board(board)

def collect_victory_lines(board):
  row1 = board[0]
  row2 = board[1]
  row3 = board[2]
  col1 = [ board[0][0], board[1][0], board[2][0] ]
  col2 = [ board[0][1], board[1][1], board[2][1] ]
  col3 = [ board[0][2], board[1][2], board[2][2] ]
  diag1 = [ board[0][0], board[1][1], board[2][2] ]
  diag2 = [ board[0][2], board[1][1], board[2][0] ]
  return [row1, row2, row3, col1, col2, col3, diag1, diag2]

def check_for_win(turn, board):
  victory = [turn, turn, turn]   # for everything, there is a season
  victory_lines = collect_victory_lines(board)
  for line in victory_lines:
    if line == victory:
     print "%s wins the game!" % turn
     return True

# ai player functions

def ai_turn(turn, board):
  selection = calculate_best_selection(turn, board)
  valid_moves = set_valid_moves(board)
  if selection not in valid_moves:
    selection = valid_moves[0]
  for row in board:
    if selection in row:
      index = row.index(selection)
      row[index] = turn
      break
  print_board(board)

def determine_enemy(turn):
  if turn == "X":
    return "O"
  elif turn == "O":
    return "X"

def analyze_offense(turn, board):
  enemy = determine_enemy(turn)
  offense_values = { "1":0.0, "2":0.0, "3":0.0, "4":0.0, "5":0.0, "6":0.0, "7":0.0, "8":0.0, "9":0.0 }
  victory_lines = collect_victory_lines(board)

  for key in offense_values:
    for line in victory_lines:
      if key in line:
        enemy_count = line.count(enemy)
        self_count = line.count(turn)

        if enemy in line:
          offense_values[key] += 0.0
        elif turn in line:
          if enemy in line:
            offense_values[key] += 0.0
          elif self_count > 1:
            offense_values[key] += 2.0
          else:
            offense_values[key] += 0.49
        else:
            offense_values[key] += 0.33

  return offense_values

def analyze_defence(turn, board):
  enemy = determine_enemy(turn)
  defense_values = { "1":0.0, "2":0.0, "3":0.0, "4":0.0, "5":0.0, "6":0.0, "7":0.0, "8":0.0, "9":0.0 }
  victory_lines = collect_victory_lines(board)

  for key in defense_values:
    for line in victory_lines:
      if key in line:
        enemy_count = line.count(enemy)
        self_count = line.count(turn)

        if enemy in line:
          if turn in line:
            defense_values[key] += 0.0
          elif enemy_count == 2:
            defense_values[key] += 0.99
          elif enemy_count == 1:
            defense_values[key] += 0.33

  return defense_values

def print_analysis(offense, defense):
  print "  OFFENSE"
  print " ".join("%.2f" % x for x in [offense["1"], offense["2"], offense["3"]])
  print " ".join("%.2f" % x for x in [offense["4"], offense["5"], offense["6"]])
  print " ".join("%.2f" % x for x in [offense["7"], offense["8"], offense["9"]])
  print "  DEFENSE"
  print " ".join("%.2f" % x for x in [defense["1"], defense["2"], defense["3"]])
  print " ".join("%.2f" % x for x in [defense["4"], defense["5"], defense["6"]])
  print " ".join("%.2f" % x for x in [defense["7"], defense["8"], defense["9"]])

def calculate_best_selection(turn, board):
  offense_values = analyze_offense(turn, board)
  defense_values = analyze_defence(turn, board)

  print_analysis(offense_values, defense_values)

  best_selection = ""
  best_selection_value = 0.0
  for key in offense_values:
    if offense_values[key] >= best_selection_value:
      best_selection = key
      best_selection_value = offense_values[key]

  for key in defense_values:
    if defense_values[key] >= best_selection_value:
      best_selection = key
      best_selection_value = defense_values[key]

  print "selection: %s" % best_selection
  print "value: %.2f" % best_selection_value

  return best_selection









# main function call

human = "O"
ask_to_play(human)

