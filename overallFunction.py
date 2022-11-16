## Import Things


###########################################################################################################################################
## Complete Reset Functions
# Grey Circle Base

# %%
from greyCircleBracket import make_grey_bracket
make_grey_bracket()

###########################################################################################################################################
## Initialize Teams, Series, and Brackets
# Read Teams from admin side (For now reading the script)
from initializeTeams    import teams

# Initialize Series Data (Mostly hardcoded)
from initializeSeries   import series

# Read data saved from individual bracket entries
from initializeBrackets import brackets

# Generate Base Bracket Graphics (Needs the teams info)


# Generate Master Bracket Graphics (Resave Base as Master)


# Generate Individual Brackets Graphics


###########################################################################################################################################
## Update Functions
from scores import scores_all

# Update Series (and Teams)
from updateSeries import updateSeries as updateSeries
updateSeries(series,teams,scores_all)

# Update Individual Bracket Points
from updatePoints import updatePoints as updatePoints
updatePoints(series,teams,brackets)

# Update Individual Bracket Graphics


# Update Master Bracket


###########################################################################################################################################
## Print Bracket Results


# %%

