from PIL import Image
import numpy as np

def updateIndividualBracketsGraphics(series,brackets):
    numSeries   = len(series)
    numBrackets = len(brackets)
    offset = 50
    
    # Loop through all brackets
    for bb in range(numBrackets):
        # Open individual's bracket
        currentBracket = Image.open("BracketResults/" + brackets[bb].name + "Bracket.png")
        greenCir = Image.open("BracketLogos/GreenCircle.png")
        redX     = Image.open("BracketLogos/RedX.png")
        
        # Loop through all series
        for ss in range(numSeries):
            if brackets[bb].ChoiceMatrix[ss] == 1:
                currentBracket.paste(greenCir , tuple(series[ss].XYPos-offset), greenCir )
                
            elif brackets[bb].ChoiceMatrix[ss] == 0:
                currentBracket.paste(redX , tuple(series[ss].XYPos), redX )
            # else == Nan
                # Don't do anything
        
        currentBracket.save("BracketResults/" + brackets[bb].name + "Bracket.png")
        #print(brackets[bb].name)
        #display(currentBracket)