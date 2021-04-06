import pandas as pd
import nbtlib


def main():
    nbt_file = nbtlib.load('scoreboard.dat')
    scores = pd.DataFrame()
    objectives = pd.Series(dtype=str)

    for score in nbt_file.root['data']['PlayerScores']:
        scores.loc[str(score['Objective']), str(score['Name'])] = int(score['Score'])

    scores.to_csv('scoreboard_scores.csv')

    for obj in nbt_file.root['data']['Objectives']:
        objectives[str(obj['Name'])] = str(obj['CriteriaName'])

    objectives.to_csv('scoreboard_objectives.csv')


if __name__ == '__main__':
    main()
