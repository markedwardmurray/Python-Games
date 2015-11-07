# This is a program for playing Battlship!
# By Mark Edward Murray

import string

def new_game():
  ocean = make_ocean(10, 10)
  print_ocean(ocean)
  fleet = arrange_fleet(ocean)
  print_ocean(ocean)
  hits = []
  for x in range(100):
    print "Turn: %d" % x
    fire_shot(fleet, ocean, hits)
    print_ocean(ocean)
    num_of_ships = evaluate_fleet(fleet, hits)
    if num_of_ships > 0:
      print "There are %i ships remaining." % num_of_ships
    else:
      break
  print "The fleet has been sunk! You win."
  ask_to_play()

# synthesis functions

def print_ocean(ocean):
  for row in ocean:
    print " ".join(row)

def make_ocean(width, height):
  ocean = []
  header = ["--"]
  letters = string.uppercase[:width]
  for c in letters:
    header.append(c)
  ocean.append(header)
  i = 1
  for x in range(height):
    ocean.append( [ "%02d" % i ] + [ "~" ] * width  )
    i += 1
  return ocean

def arrange_fleet(ocean):
  occupied = []
  fleet = []
  print "Deploy your carrier (length 5)."
  carrier = deploy_ship(5, ocean, occupied)
  fleet.append(carrier)
  for ship in fleet:
    print ship
  print "Deploy your battleship (length 4)."
  battleship = deploy_ship(4, ocean, occupied)
  fleet.append(battleship)
  for ship in fleet:
    print ship
  print "Deploy your cruiser (length 3)."
  cruiser = deploy_ship(3, ocean, occupied)
  fleet.append(cruiser)
  for ship in fleet:
    print ship
  print "Deploy your submarine (length 3)."
  submarine = deploy_ship(3, ocean, occupied)
  fleet.append(submarine)
  for ship in fleet:
    print ship
  print "Deploy your patrol boat (length 2)."
  patrol_boat = deploy_ship(2, ocean, occupied)
  fleet.append(patrol_boat)
  for ship in fleet:
    print ship
  return fleet

def deploy_ship(length, ocean, occupied):
  direction = user_input_valid_direction()
  column = user_input_ship_column(length, direction, ocean)
  row = user_input_ship_row(length, direction, ocean)
  ship = []
  # populate ship coordinates
  if direction == "V":
    for x in range(length):
      ship.append([column, str(int(row) + x) ])
  elif direction == "H":
    header = ocean[0]
    column_index = header.index(column)
    for x in range(length):
      col = header[column_index + x]
      ship.append([col, row])
  # check for conflict in ship placement
  for coordinate in ship:
    if coordinate in occupied:
      print "That placement conflicts with another vessel. Try again"
      print ship
      ship = deploy_ship(length, ocean, occupied)
  # track ship coordinates in the occupied list
  for coordinate in ship:
    occupied.append(coordinate)
  return ship

# combat functions

def fire_shot(fleet, ocean, hits):
  target = user_input_get_unique_target(ocean)
  print target
  column = target[0]
  row = target[1]
  header = ocean[0]
  column_index = header.index(column)
  is_hit = False
  for ship in fleet:
    if target in ship:
      is_hit = True
      ship_index = fleet.index(ship)
      ship_name = ship_name_for_index(ship_index)
      print "Hit!"
      ocean[int(row)][column_index] = "#"
      hits.append(target)
      ship_is_sunk = check_if_sunk(ship, hits)
      if ship_is_sunk == True:
        print "You sunk the %s!" % ship_name
      else:
        print "You hit the %s!" % ship_name
  if is_hit == False:
    print "Miss!"
    ocean[int(row)][column_index] = "O"

def check_if_sunk(ship, hits):
  for coordinate in ship:
    if coordinate not in hits:
      return False
  return True

def evaluate_fleet(fleet, hits):
  active_ships = 0
  for ship in fleet:
    for coordinate in ship:
      if coordinate not in hits:
        active_ships += 1
        break
  return active_ships

def ship_name_for_index(index):
  if index == 0:
    return "CARRIER"
  elif index == 1:
    return "BATTLESHIP"
  elif index == 2:
    return "CRUISER"
  elif index == 3:
    return "SUBMARINE"
  elif index == 4:
    return "PATROL BOAT"
  else:
    return "(ship_name_error)"

# user input functions

def user_input_valid_column(ocean):
  header = list(ocean[0])
  header.pop(0)
  column_string = raw_input("Select target column (%s-%s): " % (header[0], header[-1] ))
  valid_columns = header
  column_string = column_string.upper()
  if column_string not in valid_columns:
    print "That is not a valid column."
    column_string = user_input_valid_column(ocean)
  return column_string

def user_input_valid_row(ocean):
  width = len(ocean) - 1
  row_numbers = range(len(ocean))
  row_numbers.pop(0)
  valid_rows = [format(x,'d') for x in row_numbers]
  row_string = raw_input("Select target row (%s-%s): " % (valid_rows[0], valid_rows[-1] ))
  if row_string not in valid_rows:
    print "That is not a valid row."
    row_string = user_input_valid_row(ocean)
  return row_string

def user_input_valid_direction():
  direction = raw_input("Select ship direction (V or H): ")
  direction = direction.upper()
  valid_directions = [ "V", "H" ]
  if direction not in valid_directions:
    print "That is not a valid direction."
    direction = user_input_valid_direction()
  return direction

def user_input_ship_column(length, direction, ocean):
  if direction == "V":
    return user_input_valid_column(ocean)
  elif direction == "H":
    header = list(ocean[0])
    header.pop(0)
    counter = 1
    while counter < length:
      header.pop()
      counter += 1
    column_string = raw_input("Select target column (%s-%s): " % (header[0], header[-1] ))
    valid_columns = header
    column_string = column_string.upper()
    if column_string not in valid_columns:
      print "That is not a valid column."
      column_string = user_input_ship_column(length, direction, ocean)
    return column_string
  else:
    print "direction error"

def user_input_ship_row(length, direction, ocean):
  if direction == "H":
    return user_input_valid_row(ocean)
  elif direction == "V":
    width = len(ocean) - 1
    row_numbers = range(len(ocean))
    row_numbers.pop(0)
    counter = 1
    while counter < length:
      row_numbers.pop()
      counter += 1
    valid_rows = [format(x,'d') for x in row_numbers]
    row_string = raw_input("Select target row (%s-%s): " % (valid_rows[0], valid_rows[-1] ))
    if row_string not in valid_rows:
      print "That is not a valid row."
      row_string = user_input_ship_row(length, direction, ocean)
    return row_string
  else:
    print "direction error"

def user_input_yes_or_no():
  user_input = raw_input("y/n: ")
  if user_input.lower() == "y" or user_input.lower() == "yes":
    return True
  elif user_input.lower() == "n" or user_input.lower() == "no":
    return False
  else:
    print "This is a 'yes' or 'no' question, silly."
    return user_input_yes_or_no()

def user_input_get_unique_target(ocean):
  column = user_input_valid_column(ocean)
  row = user_input_valid_row(ocean)
  header = ocean[0]
  column_index = header.index(column)
  if ocean[int(row)][column_index] == "~":
    return [column, row]
  else:
    print "You have already fired on that coordinate."
    return user_input_get_unique_target(ocean)



def ask_to_play():
  print "Shall we play a game?"
  user_input = user_input_yes_or_no()
  if user_input == True:
    new_game()
  else:
    print "You would have lost anyway."
    quit()

# initial function call

ask_to_play()