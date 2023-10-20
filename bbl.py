import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

# Read csvs
plays = pd.read_csv('data/plays.csv')
week1 = pd.read_csv('data/week1.csv')

# Create DFs for plays and weekly data
plays = plays[["gameId", "playId", "possessionTeam", "playDescription", "passResult", "personnelO", "offenseFormation", "personnelD", "defendersInBox", "pff_passCoverage"]]
week1 = week1[["gameId", "playId", "nflId", "frameId", "team", "playDirection", "x", "y", "s", "a", "dis", "o", "dir"]]

# Drop all non-first frame records (only need pre-snap player location)
week1 = week1[week1.frameId == 1]

# Create dictionary of plays, where each key is a list of tuples of tuples
# play: [([x1, x2, xn], [y1, y2, y3]), ([x1, x2, xn], [y1, y2, y3]), ([x1], [y1])]
playDict = {}

for playNum in week1.playId.unique():
    play = week1[week1.playId == playNum]

    teams = play.team.unique()

    # teams = np.delete(teams, np.where(teams == 'football'))

    # football = play[play.team == 'football']
    # offense = play[play.team == teams[0]]
    # defense = play[play.team == teams[1]]

    # footballX = football['x'].values.flatten().tolist()
    # footballY = football['y'].values.flatten().tolist()
    # offX = offense['x'].values.flatten().tolist()
    # offY = offense['y'].values.flatten().tolist()
    # defX = defense['x'].values.flatten().tolist()
    # defY = defense['y'].values.flatten().tolist()

    # playDict[playNum] = [[footballX, footballY], [offX, offY], [defX, defY]]

    # # plt.scatter(playDict[playNum][1][0], playDict[playNum][1][1], c='blue') 

    # # plt.scatter(playDict[playNum][2][0], playDict[playNum][2][1], c='red') 

    # # plt.scatter(playDict[playNum][0][0], playDict[playNum][0][1], c='brown') 

    # # plt.axvline(x=playDict[playNum][0][0][0], c='black')

    # # plt.show() 