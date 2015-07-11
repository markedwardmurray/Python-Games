# A 3-D tic-tac-toe game by Mark Edward Murray

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
    new_game()
  else:
    print "Goodbye."

def new_game():
  cube = new_3x3x3_cube()
  turn = "#"
  display_cube_layers(cube)
  display_cube_faces(cube)
  for counter in range(26):
    if turn == "#":
      human_turn(turn, cube)
    elif turn == "~":
      human_turn(turn, cube)
    score = tally_score(cube)
    display_score(score)          # <-- will resume here, check win
    turn = switch_turns(turn)
  print "The game is over."
  ask_to_play()

def tally_score(cube):
  victory_lines = collect_victory_lines(cube)
  #display_victory_lines(victory_lines)         #dev line
  victory_octothorpe = [ "#" , "#" , "#" ]
  victory_tilde =      [ "~" , "~" , "~" ]
  octothorpe_lines = 0
  tilde_lines      = 0
  for line in victory_lines:
    if line == victory_octothorpe:
      octothorpe_lines += 1
    elif line == victory_tilde:
      tilde_lines      += 1
  return { "#":octothorpe_lines, "~":tilde_lines }

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
  print "       SCORE"
  print "   # : %d | ~ : %d" % ( score["#"] , score["~"] )
  print " "

def switch_turns(turn):
  if turn == "#":
    turn = "~"
  elif turn == "~":
    turn = "#"
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
  invalidating_symbols = [ "-", "#", "~" ]
  valid_moves = []
  for layer in cube:
    for row in layer:
      for box in row:
        if box not in invalidating_symbols:
          valid_moves.append(box)
  return valid_moves

# main function call
ask_to_play()
