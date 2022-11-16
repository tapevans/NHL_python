## Generate Base Bracket
from PIL import Image
import numpy as np

def initializeBaseBracketGraphics(teams):
    numTeams = len(teams)
    
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
    
    r,c = Round0_vec.shape
    
    # Open all team logos
    Logo_vec = []
    for i in range(numTeams):
        str = "BracketLogos/"+ teams[i].name + "Circle.png"
        Logo_vec.append( Image.open(str) )
    
    # Open the greyCircle image
    Base = Image.open("BracketResults\GreyBase.png")
    
    # Add all teams to grey circle
    for i in range(numTeams):
        Base.paste( Logo_vec[i] , tuple(Round0_vec[i]) )
        
#     display(Base)
    Base.save("BracketResults\BaseBracket.png")
    Base.save("BracketResults\MasterBracket.png")