import numpy as np

def updateSeries(series,teams,scores_all):
    ## Initialize values
    numTeams    = len(teams)
    numSeries   = len(series)
    
    round1 = 8
    round2 = 12
    round3 = 14
    round4 = 15
    
    ## Save scores to series objects
    for i in range(numSeries):
        series[i].Score = scores_all[i,:,:]
    
    ########################################################################################################################
    
    ## Update based on scores: Round 1
    for i in np.arange(0,round1,1):
        # Determine the winner
        series[i].updateWins()

        # Determine if series is complete
        series[i].updateComplete()

        # Eliminate Losers
        for j in range(numTeams):
            if series[i].Loser == teams[j].name:
                teams[j].elimFunc()
        
    ## Check if Round 2 matchups are set
    for i in np.arange(round1,round2,1):
        if (series[(series[i].SeriesDep[0])-1].isComplete and series[(series[i].SeriesDep[1])-1].isComplete):
            series[i].isMatchupSet = True
            
            # Find winners
            for j in range(numTeams):
                if teams[j].name == series[(series[i].SeriesDep[0])-1].Winner:
                    idx_upperTeam = j
                elif teams[j].name == series[(series[i].SeriesDep[1])-1].Winner:
                    idx_lowerTeam = j
                    
            if teams[idx_upperTeam].DivisionRank < teams[idx_lowerTeam].DivisionRank:
                series[i].HomeTeam = teams[idx_upperTeam].name
                series[i].AwayTeam = teams[idx_lowerTeam].name
                series[i].HomePreviousSeries = (series[i].SeriesDep[0])-1
                series[i].AwayPreviousSeries = (series[i].SeriesDep[1])-1
            else:
                series[i].HomeTeam = teams[idx_lowerTeam].name
                series[i].AwayTeam = teams[idx_upperTeam].name
                series[i].HomePreviousSeries = (series[i].SeriesDep[1])-1
                series[i].AwayPreviousSeries = (series[i].SeriesDep[0])-1
                
    ## Determine if Round 2 should be analyzed
    continueUpdate = 0
    for i in np.arange(round1,round2,1):
        continueUpdate = continueUpdate + series[i].isMatchupSet
        
#     print(continueUpdate)
    
    ########################################################################################################################
    
    ## Do Round 2 update
    if continueUpdate > 0:
        for i in np.arange(round1,round2,1):
            # Determine the winner
            series[i].updateWins()

            # Determine if series is complete
            series[i].updateComplete()

            # Eliminate Losers
            for j in range(numTeams):
                if series[i].Loser == teams[j].name:
                    teams[j].elimFunc()
                    
        ## Check if Round 3 matchups are set
        for i in np.arange(round2,round3,1):
            if (series[(series[i].SeriesDep[0])-1].isComplete and series[(series[i].SeriesDep[1])-1].isComplete):
                series[i].isMatchupSet = True

                # Find winners
                for j in range(numTeams):
                    if teams[j].name == series[(series[i].SeriesDep[0])-1].Winner:
                        idx_upperTeam = j
                    elif teams[j].name == series[(series[i].SeriesDep[1])-1].Winner:
                        idx_lowerTeam = j

                if teams[idx_upperTeam].RegularSeasonRank < teams[idx_lowerTeam].RegularSeasonRank:
                    series[i].HomeTeam = teams[idx_upperTeam].name
                    series[i].AwayTeam = teams[idx_lowerTeam].name
                    series[i].HomePreviousSeries = (series[i].SeriesDep[0])-1
                    series[i].AwayPreviousSeries = (series[i].SeriesDep[1])-1
                else:
                    series[i].HomeTeam = teams[idx_lowerTeam].name
                    series[i].AwayTeam = teams[idx_upperTeam].name
                    series[i].HomePreviousSeries = (series[i].SeriesDep[1])-1
                    series[i].AwayPreviousSeries = (series[i].SeriesDep[0])-1
    
    ## Determine if Round 3 should be analyzed
    continueUpdate = 0
    for i in np.arange(round2,round3,1):
        continueUpdate = continueUpdate + series[i].isMatchupSet
        
#     print(continueUpdate)
    
    ########################################################################################################################
    
    ## Do Round 3 update
    if continueUpdate > 0:
        for i in np.arange(round2,round3,1):
            # Determine the winner
            series[i].updateWins()

            # Determine if series is complete
            series[i].updateComplete()

            # Eliminate Losers
            for j in range(numTeams):
                if series[i].Loser == teams[j].name:
                    teams[j].elimFunc()
                    
        ## Check if Round 4 matchups are set
        for i in np.arange(round3,round4,1):
            if (series[(series[i].SeriesDep[0])-1].isComplete and series[(series[i].SeriesDep[1])-1].isComplete):
                series[i].isMatchupSet = True

                # Find winners
                for j in range(numTeams):
                    if teams[j].name == series[(series[i].SeriesDep[0])-1].Winner:
                        idx_upperTeam = j
                    elif teams[j].name == series[(series[i].SeriesDep[1])-1].Winner:
                        idx_lowerTeam = j

                if teams[idx_upperTeam].RegularSeasonRank < teams[idx_lowerTeam].RegularSeasonRank:
                    series[i].HomeTeam = teams[idx_upperTeam].name
                    series[i].AwayTeam = teams[idx_lowerTeam].name
                    series[i].HomePreviousSeries = (series[i].SeriesDep[0])-1
                    series[i].AwayPreviousSeries = (series[i].SeriesDep[1])-1
                else:
                    series[i].HomeTeam = teams[idx_lowerTeam].name
                    series[i].AwayTeam = teams[idx_upperTeam].name
                    series[i].HomePreviousSeries = (series[i].SeriesDep[1])-1
                    series[i].AwayPreviousSeries = (series[i].SeriesDep[0])-1
                    
    ########################################################################################################################
    
    ## Determine if Round 4 should be analyzed
    continueUpdate = 0
    for i in np.arange(round3,round4,1):
        continueUpdate = continueUpdate + series[i].isMatchupSet
        
#     print(continueUpdate)
    
    ## Do Round 4 update
    if continueUpdate > 0:
        for i in np.arange(round3,round4,1):
            # Determine the winner
            series[i].updateWins()

            # Determine if series is complete
            series[i].updateComplete()

            # Eliminate Losers
            for j in range(numTeams):
                if series[i].Loser == teams[j].name:
                    teams[j].elimFunc()
