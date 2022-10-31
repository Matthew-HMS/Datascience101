import random

class MyRoulette():
  def __init__(self):
      self.pockets = []
      for i in range(1, 37):
          self.pockets.append(i)
      self.ball = None
      self.pocketOdds = len(self.pockets) - 1
  def spin(self):
      self.ball = random.choice(self.pockets)
  def betPocket(self, pocket, amt):
      if str(pocket) == str(self.ball):
          return amt*self.pocketOdds
      else: return -amt
  def __str__(self):
      return 'My Roulette'

def playRoulette(game, numSpins, pocket, bet, toPrint):
  totPocket = 0
  for i in range(numSpins):
      game.spin()
      totPocket += game.betPocket(pocket, bet)
  if toPrint:
      print(numSpins, 'spins of', game)
      print('Expected return betting', pocket, '=',\
            str(100*totPocket/numSpins) + '%\n')
  return (totPocket/numSpins)

def findPocketReturn(game, numTrials, trialSize, toPrint, pocket, bet):
  pocketReturns = []
  for t in range(numTrials):
      trialVals = playRoulette(game, trialSize, pocket, bet, toPrint)
      pocketReturns.append(trialVals)
  return pocketReturns

# Monte Carlo simulation begins.
random.seed(0)
numTrials = 20
# Instantiate the Roulette game. 
game = MyRoulette()
myPocket = 7
myBet = 1
for numSpins in (1000, 10000, 100000, 1000000,10000000,100000000):
  expReturn = 0
  print('\nSimulate', numTrials, 'trials of', numSpins, 'spins each')
  # The list of my simulation results.
  pocketReturns = findPocketReturn(game, numTrials, numSpins, False, myPocket, myBet)
  # Please implement the following one-liner, the expected return.
  for i in pocketReturns:
    expReturn += i
  expReturn = expReturn/numTrials
  print('Exp. return for', game, '=', str(round(expReturn, 6)) + '%')
  print(pocketReturns)