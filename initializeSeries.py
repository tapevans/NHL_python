import numpy as np

from Class_Header import Series
#print(dir(Series))
## Initialize Series Data
series = []

for i in range(15):
  #print(i)
  series.append( Series(i+1) )

# Set the first round
# Series 1
i = 0
series[i].HomeTeam = 'Avalanche'
series[i].AwayTeam = 'Predators'
series[i].HomePreviousSeries = 1
series[i].AwayPreviousSeries = 2
series[i].isMatchupSet = True
series[i].XYPos = np.array([800 , 550])

# Series 2
i = i+1
series[i].HomeTeam = 'Wild'
series[i].AwayTeam = 'Blues'
series[i].HomePreviousSeries = 3
series[i].AwayPreviousSeries = 4
series[i].isMatchupSet = True
series[i].XYPos = np.array([800 , 1850])

# Series 3
i = i+1
series[i].HomeTeam = 'Flames'
series[i].AwayTeam = 'Stars'
series[i].HomePreviousSeries = 5
series[i].AwayPreviousSeries = 6
series[i].isMatchupSet = True
series[i].XYPos = np.array([800 , 3350])

# Series 4
i = i+1
series[i].HomeTeam = 'Oilers'
series[i].AwayTeam = 'Kings'
series[i].HomePreviousSeries = 7
series[i].AwayPreviousSeries = 8
series[i].isMatchupSet = True
series[i].XYPos = np.array([800 , 4650])

# Series 5
i = i+1
series[i].HomeTeam = 'Panthers'
series[i].AwayTeam = 'Capitals'
series[i].HomePreviousSeries = 9
series[i].AwayPreviousSeries = 10
series[i].isMatchupSet = True
series[i].XYPos = np.array([4400 , 550])

# Series 6
i = i+1
series[i].HomeTeam = 'Maple Leafs'
series[i].AwayTeam = 'Lightning'
series[i].HomePreviousSeries = 11
series[i].AwayPreviousSeries = 12
series[i].isMatchupSet = True
series[i].XYPos = np.array([4400 , 1850])

# Series 7
i = i+1
series[i].HomeTeam = 'Hurricanes'
series[i].AwayTeam = 'Bruins'
series[i].HomePreviousSeries = 13
series[i].AwayPreviousSeries = 14
series[i].isMatchupSet = True
series[i].XYPos = np.array([4400 , 3350])

# Series 8
i = i+1
series[i].HomeTeam = 'Rangers'
series[i].AwayTeam = 'Penguins'
series[i].HomePreviousSeries = 15
series[i].AwayPreviousSeries = 16
series[i].isMatchupSet = True
series[i].XYPos = np.array([4400 , 4650])

######################################
# Set Series 9-15 dependencies
# Series 9
i = i+1
series[i].SeriesDep = np.array([1,2])
series[i].XYPos = np.array([1400 , 1200])

# Series 10
i = i+1
series[i].SeriesDep = np.array([3,4])
series[i].XYPos = np.array([1400 , 4000])

# Series 11
i = i+1
series[i].SeriesDep = np.array([5,6])
series[i].XYPos = np.array([3800 , 1200])

# Series 12
i = i+1
series[i].SeriesDep = np.array([7,8])
series[i].XYPos = np.array([3800 ,4000 ])

# Series 13
i = i+1
series[i].SeriesDep = np.array([9,10])
series[i].XYPos = np.array([2000 , 2600])

# Series 14
i = i+1
series[i].SeriesDep = np.array([11,12])
series[i].XYPos = np.array([3200 ,2600 ])

# Series 15
i = i+1
series[i].SeriesDep = np.array([13,14])
series[i].XYPos = np.array([2600 , 4856])