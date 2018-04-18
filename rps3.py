import random
def initialize ():
  """ Helper Function: Returns the number of rounds the user wants
  Checks that the input is an integer less than 0."""
  try: 
    rounds =int(input ("How much rounds do you want to play?"))
    if (rounds <=0): raise ValueError
  except ValueError:
    print ("Please enter an integer greater than 0!")
    return initialize()
  else : return rounds
  
def user1 ():
  """ Helper Function: Returns user's choice of 1 for rock, 2 for paper, and 3 for scissor
  Checks that the input is an integer and is either 1, 2, or 3
  """
  try:
    user = int (input ("Pick 1 for rock, 2 for paper and 3 for scissor."))
    if (user == 0 or user >3): raise ValueError
  except  ValueError:
    print ("Enter either 1, 2 or 3")
    return user1()
  else: return user
def game ():
  """ Runs the logic of the game."""
  computer = random.randint(1,3)
  user = user1()
  global won
  if (Combos[(computer,user)]==0):
      print ("It's a tie!")
  if (Combos[(computer,user)]==1):
      print ("You Won! Computer picked", Options[computer])
      won += 1
  if (Combos[(computer,user)]==2):
      print ("You Lost. Computer picked", Options[computer])
won = 0 #the number of wins the user has
rounds = initialize() 
Options = {1:"Rock", 2:"Paper", 3:"Scissor"} # A dictionary where the key is the numerical choice and the value is it's word equivalent
Combos = {(1,1):0, (2,2):0, (3,3):0, (1,2):1, (2,3):1, (3,1):1, (1,3):2, (2,1):2, (3,2):2} #A dictionary of the results. Key is (computer, user)
#and value is 0 for tie, 1 for win and 2 for lost""" 
while (rounds != 0):
  rounds= rounds - 1 
  game()
print ("Thanks for playing! You won",won, "times")
quit()