import pandas as pd
import nbtlib
import time

try:
    import rich
    RICH = True
except ImportError:
    RICH = False


def print_helper(color, text):
    if RICH:
        rich.print(color + text)
    else:
        print(text)


t0 = time.perf_counter()
print_helper('[blue]', 'Loading in data..')

nbt_file = nbtlib.load('scoreboard.dat').root['data'].unpack()
scores = pd.DataFrame(columns=['Objective', 'Player', 'Score'])
objectives = pd.DataFrame(columns=['Objective', 'Type'])

print_helper('[blue]', 'Getting scores...')
scores = pd.DataFrame(nbt_file['PlayerScores'])
print_helper('[green]', '  Saving to csv')
scores.to_csv('scoreboard_scores.csv', index=False)

print_helper('[blue]', 'Getting objectives...')
objectives = pd.DataFrame(nbt_file['Objectives'])
print_helper('[green]', '  Saving to csv')

objectives.to_csv('scoreboard_objectives.csv', index=False)

elapsed = time.perf_counter() - t0
print_helper('[bold green]', f'Done in {elapsed:.3f}s')
