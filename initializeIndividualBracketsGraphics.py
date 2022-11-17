## This function is used to create the brackets for each individual entry
from PIL import Image
import numpy as np

def initializeIndividualBracketsGraphics(teams,series,brackets):
    numTeams    = len(teams)
    numSeries   = len(series)
    numBrackets = len(brackets)
    
    # Loop through all entries
    for bb in range(numBrackets):
        #print(brackets[bb].name)
        
        # Open Base Figure
        CurrentBracket = Image.open("BracketResults\BaseBracket.png")
        
        # Loop through each series and place winner in the respective spot
        for ss in range(numSeries):
            # Open logo for the chosen winner
            dasLogo = Image.open("BracketLogos/"+ brackets[bb].seriesWinners[ss] + "Circle.png")
            
            # Paste image in respective spot
            CurrentBracket.paste( dasLogo , tuple(series[ss].XYPos) )
            
        # Display/save figure
        #display(CurrentBracket)
        CurrentBracket.save("BracketResults/" + brackets[bb].name + "Bracket.png")