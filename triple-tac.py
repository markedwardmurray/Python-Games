# -*- coding: utf-8 -*-


# A 3-D tic-tac-toe game by Mark Edward Murray

import random


circle = "◉"
star = "▼"

# cube and cube-display functions

def new_3x3x3_cube():
  layer0 = [ ["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"] ]
  layer1 = [ ["J", "K", "L"], ["M", "-", "N"], ["O", "P", "Q"] ]
  layer2 = [ ["R", "S", "T"], ["U", "V", "W"], ["X", "Y", "Z"] ]
  return [ layer0, layer1, layer2 ]

def display_cube_layers(cube): #dev function
  for layer in cube:
    for row in layer:
      print " ".join(row)
    print " "

def display_cube_faces(cube):
  A = cube[0][0][0]
  B = cube[0][0][1]
  C = cube[0][0][2]
  #
  D = cube[0][1][0]
  E = cube[0][1][1]
  F = cube[0][1][2]
  #
  G = cube[0][2][0]
  H = cube[0][2][1]
  I = cube[0][2][2]
  #
  J = cube[1][0][0]
  K = cube[1][0][1]
  L = cube[1][0][2]
  #
  M = cube[1][1][0]
  N = cube[1][1][2]
  #
  O = cube[1][2][0]
  P = cube[1][2][1]
  Q = cube[1][2][2]
  #
  R = cube[2][0][0]
  S = cube[2][0][1]
  T = cube[2][0][2]
  #
  U = cube[2][1][0]
  V = cube[2][1][1]
  W = cube[2][1][2]
  #
  X = cube[2][2][0]
  Y = cube[2][2][1]
  Z = cube[2][2][2]
  #
  print " "
  print "       " + R + " " + S + " " + T
  print "       " + J + " " + K + " " + L
  print "       " + A + " " + B + " " + C
  print " "
  print R + " " + J + " " + A + "  " + A + " " + B + " " + C + "  " + C + " " + L + " " + T
  print U + " " + M + " " + D + "  " + D + " " + E + " " + F + "  " + F + " " + N + " " + W
  print X + " " + O + " " + G + "  " + G + " " + H + " " + I + "  " + I + " " + Q + " " + Z
  print " "
  print "       " + G + " " + H + " " + I
  print "       " + O + " " + P + " " + Q
  print "       " + X + " " + Y + " " + Z
  print " "
  print "       " + X + " " + Y + " " + Z
  print "       " + U + " " + V + " " + W
  print "       " + R + " " + S + " " + T
  print " "

# referee functions

def ask_to_play():
  answer = raw_input("Shall we play a game? (y/n) ")
  if answer[:1].lower() == "y":
    players = ask_number_of_players()
    if players == "2":
      new_game()
    elif players == "1":
      new_ai_game()
  else:
    print "Goodbye."

def ask_number_of_players():
  players = raw_input("How many players? (1-2) ")
  if players == "1" or players == "2":
    return players
  else:
    return ask_number_of_players()


def new_ai_game():
  cube = new_3x3x3_cube()
  turn = circle
  # display_cube_layers(cube)
  display_cube_faces(cube)
  for counter in range(26):
    if turn == circle:
      human_turn(turn, cube)
    elif turn == star:
      ai_turn(turn, cube)
    score = tally_score(cube)
    display_score(score)
    if score["attainable"] == 0:
      break
    turn = switch_turns(turn)
  display_winner(score)
  ask_to_play()


def new_game():
  cube = new_3x3x3_cube()
  turn = circle
  # display_cube_layers(cube)
  display_cube_faces(cube)
  for counter in range(26):
    if turn == circle:
      human_turn(turn, cube)
    elif turn == star:
      human_turn(turn, cube)
    score = tally_score(cube)
    display_score(score)
    if score["attainable"] == 0:
      break
    turn = switch_turns(turn)
  display_winner(score)
  ask_to_play()

def display_winner(score):
  octothorpe_lines = score[circle]
  tilde_lines = score[star]
  if octothorpe_lines > tilde_lines:
    print "     %s has won!" % circle
  elif tilde_lines > octothorpe_lines:
    print "     %s has won!" % star
  elif tilde_lines == octothorpe_lines:
    print "       Draw!"


def tally_score(cube):
  victory_lines = collect_victory_lines(cube)
  #display_victory_lines(victory_lines)         #dev line
  victory_circle = [ circle , circle , circle ]
  victory_star   = [ star , star , star ]
  circle_lines = 0
  star_lines   = 0
  attainable_lines = 0
  for line in victory_lines:
    if line == victory_circle:
      circle_lines += 1
    elif line == victory_star:
      star_lines   += 1
    elif circle not in line or star not in line:
      attainable_lines += 1
  return { circle:circle_lines, star:star_lines, "attainable":attainable_lines }

def display_victory_lines(victory_lines): #dev function
  counter = 0
  for line in victory_lines:
    counter += 1
    print counter
    print line
  
def collect_victory_lines(cube):
  victory_lines = []
  # 8 x-axis
  for layer in cube:
    for row in layer:
      if row != cube[1][1]:
        victory_lines.append(row)
  # 8 y-axis
  for layer in cube:
    column0 = [ layer[0][0] , layer[1][0] , layer[2][0] ]
    column1 = [ layer[0][1] , layer[1][1] , layer[2][1] ]
    column2 = [ layer[0][2] , layer[1][2] , layer[2][2] ]
    victory_lines.append(column0)
    if layer != cube[1]:
      victory_lines.append(column1)
    victory_lines.append(column2)
  # 8 z-axis
  stack1 = [ cube[0][0][0] , cube[1][0][0] , cube[2][0][0] ]
  stack2 = [ cube[0][0][1] , cube[1][0][1] , cube[2][0][1] ]
  stack3 = [ cube[0][0][2] , cube[1][0][2] , cube[2][0][2] ]
  stack4 = [ cube[0][1][0] , cube[1][1][0] , cube[2][1][0] ]
  stack5 = [ cube[0][1][2] , cube[1][1][2] , cube[2][1][2] ]
  stack6 = [ cube[0][2][0] , cube[1][2][0] , cube[2][2][0] ]
  stack7 = [ cube[0][2][1] , cube[1][2][1] , cube[2][2][1] ]
  stack8 = [ cube[0][2][2] , cube[1][2][2] , cube[2][2][2] ]
  stacks = [ stack1 , stack2, stack3, stack4, stack5, stack6, stack7, stack8 ]
  for stack in stacks:
    victory_lines.append(stack)
  # 12 face diagonals
  cube_faces = organize_cube_faces(cube)
  for face in cube_faces:
    diag1 = [ face[0][0], face[1][1], face[2][2] ]
    victory_lines.append(diag1)
    diag2 = [ face[0][2], face[1][1], face[2][0] ]
    victory_lines.append(diag2)
  return victory_lines

def organize_cube_faces(cube):
  A = cube[0][0][0]
  B = cube[0][0][1]
  C = cube[0][0][2]
  #
  D = cube[0][1][0]
  E = cube[0][1][1]
  F = cube[0][1][2]
  #
  G = cube[0][2][0]
  H = cube[0][2][1]
  I = cube[0][2][2]
  #
  J = cube[1][0][0]
  K = cube[1][0][1]
  L = cube[1][0][2]
  #
  M = cube[1][1][0]
  N = cube[1][1][2]
  #
  O = cube[1][2][0]
  P = cube[1][2][1]
  Q = cube[1][2][2]
  #
  R = cube[2][0][0]
  S = cube[2][0][1]
  T = cube[2][0][2]
  #
  U = cube[2][1][0]
  V = cube[2][1][1]
  W = cube[2][1][2]
  #
  X = cube[2][2][0]
  Y = cube[2][2][1]
  Z = cube[2][2][2]
  #
  back =   [[ R , S , T ] , [ J , K , L ] , [ A , B , C ]]
  left =   [[ R , J , A ] , [ U , M , D ] , [ X , O , G ]]
  top =    [[ A , B , C ] , [ D , E , F ] , [ G , H , I ]]
  right =  [[ C , L , T ] , [ F , N , W ] , [ I , Q , Z ]]
  front =  [[ G , H , I ] , [ O , P , Q ] , [ X , Y , Z ]]
  bottom = [[ X , Y , Z ] , [ U , V , W ] , [ R , S , T ]]
  #
  return [ back, left, top, right, front, bottom ]

def display_score(score):
  print "   %s   SCORE   %s" % ( circle , star )
  print "   %d   [ %2d]   %d" % ( score[circle] , score["attainable"], score[star] )
  print " "

def switch_turns(turn):
  if turn == circle:
    turn = star
  elif turn == star:
    turn = circle
  return turn

# human turn functions

def human_turn(turn, cube):
  selection = ask_valid_selection(turn, cube)
  for layer in cube:
    for row in layer:
      if selection in row:
        index = row.index(selection)
        row[index] = turn
        break
  display_cube_faces(cube)

def ask_valid_selection(turn, cube):
  valid_moves = retrieve_valid_moves(cube)
  # print valid_moves
  selection = raw_input("Turn: %s -- Select a cube to claim by entering A - Z: " % turn)
  selection = selection.upper()
  if selection in valid_moves:
     return selection
  else:
     return ask_valid_selection(turn, cube)

def retrieve_valid_moves(cube):
  invalidating_symbols = [ "-", circle, star ]
  valid_moves = []
  for layer in cube:
    for row in layer:
      for box in row:
        if box not in invalidating_symbols:
          valid_moves.append(box)
  return valid_moves

# ai turn functions

def ai_turn(turn, cube):
  selection = determine_selection(turn, cube)
  for layer in cube:
    for row in layer:
      if selection in row:
        index = row.index(selection)
        row[index] = turn
        break
  display_cube_faces(cube)

def determine_selection(turn, cube):
  offense_values = analyze_offense(turn, cube)
  defense_values = analyze_defense(turn, cube)
  combined_values = {}
  for move in offense_values:
    value = offense_values[move] + defense_values[move]
    combined_values[move] = value
    #print "%s - %.2f + %.2f = %.2f" % ( move , offense_values[move] , defense_values[move] , combined_values[move] )
  highest_value = 0.0
  for move in combined_values:
    if combined_values[move] > highest_value:
      highest_value = combined_values[move]
  #print "highest_value = %.2f" % highest_value
  best_moves = []
  for move in combined_values:
    if combined_values[move] == highest_value:
      best_moves.append(move)
  #print best_moves
  selection = random.choice(best_moves)
  print "I'll take %s" % selection
  return selection

def determine_enemy(turn):
  if turn == circle:
    return star
  elif turn == star:
    return circle

def analyze_defense(turn, cube):
  enemy = determine_enemy(turn)
  valid_moves = retrieve_valid_moves(cube)
  defense_values = {}
  for move in valid_moves:
    defense_values[move] = 0.0
  #
  victory_lines = collect_victory_lines(cube)
  #
  for key in defense_values:
    for line in victory_lines:
      if key in line:
        enemy_count = line.count(enemy)
        self_count = line.count(turn)

        if enemy in line:
          if turn in line:
            defense_values[key] += 0.0
          elif enemy_count == 2:
            defense_values[key] += 0.98
          elif enemy_count == 1:
            defense_values[key] += 0.49
        elif turn not in line:
          defense_values[key] += 0.33
  #
  return defense_values

def analyze_offense(turn, cube):
  enemy = determine_enemy(turn)
  valid_moves = retrieve_valid_moves(cube)
  offense_values = {}
  for move in valid_moves:
    offense_values[move] = 0.0
  #
  victory_lines = collect_victory_lines(cube)
  #
  for key in offense_values:
    for line in victory_lines:
      if key in line:
        enemy_count = line.count(enemy)
        self_count = line.count(turn)

        if enemy in line:
          offense_values[key] += 0.0
        elif turn in line:
          if self_count == 2:
            offense_values[key] += 0.99
          elif self_count == 1:
            offense_values[key] += 0.49
        else:
            offense_values[key] += 0.33
  #
  return offense_values



# main function call

ask_to_play()


