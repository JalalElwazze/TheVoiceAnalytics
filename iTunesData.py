from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

# Read the page of links to full data
links = requests.get('http://kworb.net/cc/archive/us/')

# Parse with BS
linkSoup = BeautifulSoup(links.content, 'lxml')

# Grab tables
linkTable = linkSoup.find_all('table')

# Read with pandas
links = pd.read_html(str(linkTable), skiprows=1)
links = links[0]

# Label columns
links.columns = ['image', 'directory', 'date', 'size', 'description']
links.drop(links.index[0], inplace=True)
links.drop(['image', 'description'], axis=1, inplace=True)
link = links['directory'].as_matrix()

# Define the path
path = 'http://kworb.net/cc/archive/us/'

# Go through every file
for l in link:

    # Start timing
    start_time = time.time()

    # Define the url
    url = path + l

    # Status update
    print('Requesting', url)

    # Read the webpage
    page = requests.get(url)

    # Parse the page as a BS obejct
    soup = BeautifulSoup(page.content, 'lxml')

    # Grab table
    table = soup.find_all('table')

    # Read as df
    dfs = pd.read_html(str(table))
    dfm = dfs[0]

    # Header names
    if len(dfm.columns) == 13:
        headers = ['7d', '5d', '3d', '2d', '1d', 'now', 'name', 'peak', 'Top 10', 'Top 100', 'start', 'end', 'change']
    else:
        dfm.drop(dfm.index[0:2], inplace=True)
        headers = ['7d', '5d', '3d', '2d', '1d', 'extra_time',
                   'now', 'name', 'peak', 'Top 10', 'Top 100', 'start', 'end', 'change']

    # Name the columns and re-index
    dfm.columns = headers
    dfm.reset_index(inplace=True)

    # Extract only what we want
    dfm = dfm[['name', 'Top 100', 'end', 'change']]

    # Status update
    print('Dataframe successfuly created')
    print(dfm.head(n=3))

    # Write to csv
    filename = l.replace('.html', '.csv')
    filepath = '/Users/jalal/Documents/Python/TheVoiceAnalytics/iTunesCSV/' + filename
    dfm.to_csv(filepath)

    # Status update
    print(filename, 'successfuly logged')
    print('Total process completed in', time.time()-start_time, 'seconds')

