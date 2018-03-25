from bs4 import BeautifulSoup
import pandas as pd
import requests

# Read the wiki page which gets updated for us continously
page = requests.get('https://en.wikipedia.org/wiki/The_Voice_(U.S._TV_series)')

# Parse the page as a BS obejct
soup = BeautifulSoup(page.content, 'lxml')

# Grab all the tables
table = soup.find_all('table')

# Turn all the tables into dataframes
dfs = pd.read_html(str(table))

# Extract all the contestant dataframes
df = dfs[5:18]

# Clean up every dataframe
for i, frame in enumerate(df):
    frame.columns = frame.iloc[0]
    frame.drop(frame.index[0], inplace=True)

# Lists for all useful parameters
contestants = []
teams = []
seasons = []

# Grab info from dataframes
for i, frame in enumerate(df):
    contestants.append(frame.values)
    for k in range(frame.values.size):
        seasons.append(i+1)

# Clean contestants list
contestants = [name for sublist in contestants for name in sublist]
contestants = [name for sublist in contestants for name in sublist]

# Clean teams list
for frame in df:
    for person in contestants:
        for k in range(len(frame.index)):
            x = frame.columns[(frame == person).iloc[k]]
            x = x.format()
            if len(x) is not 0:
                teams.append(x)

teams = [peep for sublist in teams for peep in sublist]

# Create final dataframe
df = {'Contestant': contestants,
      'Season': seasons,
      'Team': teams}

df = pd.DataFrame(df)
print(df)

# Write to csv
df.to_csv('ContestantData.csv')