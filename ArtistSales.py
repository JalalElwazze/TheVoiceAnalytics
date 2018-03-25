import pandas as pd
import glob
import time

# Path to data folder
path = '/Users/jalal/Documents/Python/TheVoiceAnalytics/iTunesCSV'

# list of files
folder = glob.glob(path + '/*.csv')

# df of artists
artists = pd.read_csv('ContestantData.csv')

# List of artists
artists = artists['Contestant'].as_matrix()

# Sales array
sales = []

# Go through every artist
for name in artists:

    # Start time
    start_time = time.time()
    # Status update
    print('-'*100)
    print('Searching for', name)

    # Individual sales
    individual_sales = []
    # Go through every file
    for file in folder:

        # Make a dataframe
        df = pd.read_csv(file)

        # Drop all the NaNs
        df.fillna(value=0, inplace=True)

        # Convert all columns to strings
        df[['name', 'Top 100', 'end', 'change']] = df[['name', 'Top 100', 'end', 'change']].astype(str)

        # Search for the artists row
        row = df[df['name'].str.contains(name)]

        # Extract the end sales they earnt
        end = row['end'].as_matrix()

        # Convert data type
        end = [float(number.replace('k', '')) for number in end]

        # Sum and add to results array
        individual_sales.append(sum(end))

    # Add to total sales for this artist
    sales.append(sum(individual_sales))

    # Status update
    print('Total Sales:', sum(individual_sales))
    print('Process Completed in', time.time() - start_time, 'Seconds')

# Write the result to a csv
FullArtistData = pd.read_csv('ContestantData.csv')
FullArtistData['Total Sales'] = sales
FullArtistData.to_csv('ArtistSales.csv')
