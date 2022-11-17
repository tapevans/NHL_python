import numpy as np

# This is currently hardcoded

scores_all = np.zeros((15,2,7),order='F')

# Series 1 Avs/Preds
#scores_all[0,:,:] = np.array([
#  [2, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  #Preds
#  [7, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]) # Avs  
scores_all[0,:,:] = np.array([
  [2, 1, 3, 3, np.nan, np.nan, np.nan],  #Preds
  [7, 2, 7, 5, np.nan, np.nan, np.nan]]) # Avs               

# Series 2 Wild/Blues
#scores_all[1,:,:] = np.array([
#    [4, 2, np.nan, np.nan, np.nan, np.nan, np.nan],  # Blues
#    [0, 6, np.nan, np.nan, np.nan, np.nan, np.nan]]) # Wild
scores_all[1,:,:] = np.array([
    [4, 2, 1, 5, 5, 5, np.nan],  # Blues
    [0, 6, 5, 2, 2, 1, np.nan]]) # Wild

# Series 3 Flames/Stars
# scores_all[2,:,:] = np.array([
#  [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],    # Stars
#  [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]])   # Flames
scores_all[2,:,:] = np.array([
  [0, 2, 4, 1, 1, 4, 2],    # Stars
  [1, 0, 2, 4, 3, 2, 3]])   # Flames
    

# Series 4 Oilers/Kings
# scores_all[3,:,:] = np.array([
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # Kings
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]) # Oilers
scores_all[3,:,:] = np.array([
  [4, 0, 2, 4, 5, 2, 0],  # Kings
  [3, 6, 8, 0, 4, 4, 2]]) # Oilers
    

# Series 5 Panthers/Caps
# scores_all[4,:,:] = np.array([
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],   # Caps
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]) # Panthers
scores_all[4,:,:] = np.array([
  [4, 1, 6, 2, 3, 3, np.nan],   # Caps
  [2, 5, 1, 3, 5, 4, np.nan]]) # Panthers
    

# Series 6 Leafs/Lightning
# scores_all[5,:,:] = np.array([
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # Lightning
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]) # Leafs
scores_all[5,:,:] = np.array([
  [0, 5, 2, 7, 3, 4, 2],  # Lightning
  [5, 3, 5, 3, 4, 3, 1]]) # Leafs
    

# Series 7 Canes/Bruins
# scores_all[6,:,:] = np.array([
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # Bruins
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]) # Canes
scores_all[6,:,:] = np.array([
  [1, 2, 4, 5, 1, 5, 2],  # Bruins
  [5, 5, 2, 2, 5, 2, 3]]) # Canes
    

# Series 8 Rangers/Penguins
# scores_all[7,:,:] = np.array([
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # Penguins
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]) # Rangers
scores_all[7,:,:] = np.array([
  [4, 2, 7, 7, 3, 3, 3],  # Penguins
  [3, 5, 4, 2, 5, 5, 4]]) # Rangers
    

# Series 9 Avs/Blues
# scores_all[8,:,:] = np.array([
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # Blues
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]) # Avs
scores_all[8,:,:] = np.array([
  [2, 4, 2, 3, 5, 2, np.nan],  # Blues
  [3, 1, 5, 6, 4, 3, np.nan]]) # Avs
    

# Series 10 Flames/Oilers
# scores_all[9,:,:] = np.array([
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # Oilers
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]) # Flames
scores_all[9,:,:] = np.array([
  [6, 5, 4, 5, 5, np.nan, np.nan],  # Oilers
  [9, 3, 1, 3, 4, np.nan, np.nan]]) # Flames
    

# Series 11 Panthers/Lightning
# scores_all[10,:,:] = np.array([
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # Lightning
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]) # Panthers
scores_all[10,:,:] = np.array([
  [4, 2, 5, 2, np.nan, np.nan, np.nan],  # Lightning
  [1, 1, 1, 0, np.nan, np.nan, np.nan]]) # Panthers
    

# Series 12 Hurricanes/Rangers
# scores_all[11,:,:] = np.array([
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # Rangers
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]) # Hurricanes
scores_all[11,:,:] = np.array([
  [1, 0, 3, 4, 1, 5, 6],  # Rangers
  [2, 2, 1, 1, 3, 2, 2]]) # Hurricanes
    

# Series 13 Avs/Oilers
# scores_all[12,:,:] = np.array([
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # Oilers
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]) # Avs
scores_all[12,:,:] = np.array([
  [6, 0, 2, 5, np.nan, np.nan, np.nan],  # Oilers
  [8, 4, 4, 6, np.nan, np.nan, np.nan]]) # Avs
    

# Series 14 Rangers/Lightning
# scores_all[13,:,:] = np.array([
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # Lightning
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]) # Rangers
scores_all[13,:,:] = np.array([
  [2, 2, 3, 4, 3, 2, np.nan],  # Lightning
  [6, 3, 2, 1, 1, 1, np.nan]]) # Rangers
    

# Series 15 Avs/Lightning
# scores_all[14,:,:] = np.array([
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # Lightning
#   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]) # Avs
scores_all[14,:,:] = np.array([
 [3, 0, 6, 2, 3, 1, np.nan],  # Lightning
 [4, 7, 2, 3, 2, 2, np.nan]]) # Avs