import numpy as np

def updatePoints(series,teams,brackets):
    ## Initialize Values
    numTeams    = len(teams)
    numSeries   = len(series)
    numBrackets = len(brackets)
    
    Scoring = np.array([10, 10, 10, 10, 10, 10, 10, 10, 25, 25, 25, 25, 50, 50, 100])
    #Scoring = Scoring)
    
    for i in range(numBrackets):
#         print()
#         print()
#         print("Performing calculations for {}'s bracket".format(brackets[i].name))
        Aquired   = 0
        Potential = 0
        
#         print('Looping through all the series')
        for j in range(numSeries):
#             print()
#             print(' Series {}'.format(j+1))
#             print(' Points available for this series is {}'.format(Scoring[j]))
#             print(' This series has been completed: {}'.format(series[j].isComplete) )
            if series[j].isComplete:
#                 print('   {} are the winners of this series.'.format(series[j].Winner))
#                 print('   {} chose {} to win this series.'.format(brackets[i].name,brackets[i].seriesWinners[j]))
                if series[j].Winner == brackets[i].seriesWinners[j]:
#                     print('    {} aquired {} points for this series.'.format(brackets[i].name,Scoring[j]))
                    Aquired = Aquired + Scoring[j]
                    brackets[i].ChoiceMatrix[j] = 1
#                     print('    The value for the choiceMatrix is then {} = 1'.format(brackets[i].ChoiceMatrix[j]))
#                     print('    {} now has aquired {} points'.format(brackets[i].name,Aquired) )
                else:
#                     print('    {} aquired no points for this series.'.format(brackets[i].name))
                    brackets[i].ChoiceMatrix[j] = 0
            else:
#                 print('   Since the series is not complete then there can only be potential points')
#                 print('   {} chose {} to win this series.'.format(brackets[i].name,brackets[i].seriesWinners[j]))
                for jj in range(numTeams):
                    if brackets[i].seriesWinners[j] == teams[jj].name:
#                         print('    Found a match at index {}'.format(jj))
                        team_idx = jj
#                 print('    This team matches with index {}, team {}'.format(team_idx,teams[team_idx].name) )
                if teams[team_idx].isEliminated:
#                     print('    {} has been eliminated so no points are issued and the choice matrix is {} = 0'.format(teams[team_idx].name,brackets[i].ChoiceMatrix[j]))
                    brackets[i].ChoiceMatrix[j] = 0
                else:
#                     print('    {} has not been eliminated so {} potential points are available'.format(teams[team_idx].name,Scoring[j]))
                    Potential = Potential + Scoring[j]
                    brackets[i].ChoiceMatrix[j] = np.nan
#                     print('    {} now has {} potential points'.format(brackets[i].name,Potential) )
            
#             print('Choice matrix is now {}'.format(brackets[i].ChoiceMatrix))
            
            brackets[i].points_aquired = Aquired
            brackets[i].points_potential = Potential
            brackets[i].points_totalPossible = Aquired + Potential