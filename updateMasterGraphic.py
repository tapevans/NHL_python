from PIL import Image
import numpy as np

def updateMasterGraphic(series):
    numSeries   = len(series)
    alpha = 0.5 # alpha is between 0 and 1
    # XY positions of top left corner of the image
    Round0_vec = np.array(
        [[200,  200],
        [200,  900],
        [200,  1500],
        [200,  2200],
        [200,  3000],
        [200,  3700],
        [200,  4300],
        [200,  5000],
        [5000, 200],
        [5000, 900],
        [5000, 1500],
        [5000, 2200],
        [5000, 3000],
        [5000, 3700],
        [5000, 4300],
        [5000, 5000]])
    
    # Open Master Bracket
    MasterBracket = Image.open("BracketResults/MasterBracket.png")
    
    # Open RedX
    redX = Image.open("BracketLogos/RedX.png")
    
    for ss in range(numSeries):
        if series[ss].isComplete:
            Home = Image.open("BracketLogos/" + series[ss].HomeTeam + "Circle.png")
            Away = Image.open("BracketLogos/" + series[ss].AwayTeam + "Circle.png")
            
            if series[ss].Winner == series[ss].HomeTeam:
                # Winner
                MasterBracket.paste( Home , tuple(series[ss].XYPos) )
                
                # Loser
                GreyOut = Image.blend(Away,redX,alpha)
                if ss<8:
                    ULC_Pos = tuple(Round0_vec[series[ss].AwayPreviousSeries -1])
                else:
                    ULC_Pos = tuple(series[series[ss].AwayPreviousSeries].XYPos)
                    
                MasterBracket.paste( GreyOut , ULC_Pos )
            else:
                #Winner
                MasterBracket.paste( Away , tuple(series[ss].XYPos) ) 
                
                #Loser
                GreyOut = Image.blend(Home,redX,alpha)
                if ss<8:
                    ULC_Pos = tuple(Round0_vec[series[ss].HomePreviousSeries -1])
                else:
                    ULC_Pos = tuple(series[series[ss].HomePreviousSeries].XYPos)
                    
                MasterBracket.paste( GreyOut , ULC_Pos )

    #display(MasterBracket)
    MasterBracket.save("BracketResults/MasterBracket.png")
    
    ## Loop through series
        # Check if the series is complete
            # If the home team won
                # Grey out away team
                    #If the series(ss) is < 9 (First round), then use Round0 to grey out, can use teams index to match Round0 index
                    # Apply transparency with the X and logo, then paste that composite into bracket
                # Add home team to series(ss)
            # else 
                # Grey out home team
                    #If the series(ss) is < 9 (First round), then use Round0 to grey out, can use teams index to match Round0 index
                    # Apply transparency with the X and logo, then paste that composite into bracket
                # Add away team to series(ss) (Series.winner)