import numpy as np

class Series:
  number = 0
  HomeTeam = ''
  AwayTeam = ''
  Score = np.full((2,7),np.nan)
  HomeWins = 0
  AwayWins = 0
  SeriesDep = np.zeros((1,2))
  isMatchupSet = False
  isComplete = False
  Winner = ''
  HomePreviousSeries = 0
  AwayPreviousSeries = 0

  def __init__(self,number):
    self.number = number
    
  def updateScore(self,gameScore):
    self.Score = gameScore