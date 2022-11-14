for j in range(numTeams):
    if teams[j].isEliminated:
        print('{} has been eliminated'.format(teams[j].name))
    else:
        print('{} is alive'.format(teams[j].name))