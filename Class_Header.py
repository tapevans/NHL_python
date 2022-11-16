import numpy as np

################################################################################
#################################### Teams #####################################
################################################################################

class Team:
    isEliminated = False
    def __init__(self,name,DivisionRank,RegularSeasonRank):
        self.name = name
        self.DivisionRank = DivisionRank
        self.RegularSeasonRank = RegularSeasonRank
        self.isEliminated = False
        #BackgroundColor = [0,0,0]
        #TextColor = [0,0,0]
        #print(self.name)
    def elimFunc(self):
        self.isEliminated = True

################################################################################
#################################### Series ####################################
################################################################################

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
    Loser  = ''
    HomePreviousSeries = 0
    AwayPreviousSeries = 0
    XYPos = np.zeros(2)
    def __init__(self,number):
        self.number = number
        
    def updateWins(self):
        #print('Inside class,updateWins, homeWinArray is {}'.format(self.Score[0]<self.Score[1]) )
        #print('Inside class,updateWins, awayWinArray is {}'.format(self.Score[0]>self.Score[1]) )
        self.HomeWins = sum(self.Score[0]<self.Score[1])
        self.AwayWins = sum(self.Score[0]>self.Score[1])
    
    def checkIfComplete(self):
        return ((self.HomeWins == 4) or (self.AwayWins == 4))
    
    def updateComplete(self):
        if self.checkIfComplete():
            self.isComplete = True
            if self.HomeWins == 4:
                self.Winner = self.HomeTeam
                self.Loser  = self.AwayTeam
            else:
                self.Winner = self.AwayTeam
                self.Loser  = self.HomeTeam
    

################################################################################
################################### Brackets ###################################
################################################################################

class Bracket:
    name = ''
    seriesWinners = []
    points_aquired = 0
    points_potential = 0
    points_totalPossible = 0
    ChoiceMatrix = np.full( (15), 7.0)
    def __init__(self, name, winners):
        self.name = name
        self.seriesWinners = winners
        self.points_aquired = 0
        self.points_potential = 0
        self.points_totalPossible = 380
        self.ChoiceMatrix = np.full( (15), np.nan )
    