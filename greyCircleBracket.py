# %% 
from PIL import Image
import numpy as np

def make_grey_bracket():
    Bracket = Image.open("TempBrackets\BracketBase.png")
    #display(Bracket)

    # XY positions of top left corner of the image
    # 
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

    Grey = Image.open("BracketLogos\Grey.png")

    # Loop through all rows to get all grey circles
    for i in range(r):
        Bracket.paste(  Grey, tuple(Round0_vec[i]) )
        

    #display(Bracket)

    Bracket.save("BracketResults\GreyBase.png")

if __name__ == "__main__":
    make_grey_bracket()
# %%
