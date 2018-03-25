import pandas as pd
import glob

# Path to data folder
path = '/Users/jalal/Documents/Python/TheVoiceAnalytics/iTunesCSV'

# list of files
folder = glob.glob(path + '/*.csv')

# Artist to search
artist = 'Katy Perry'

# Read first file
sales = []

for file in folder:
    df = pd.read_csv(file)
    df.fillna(value=0, inplace=True)
    df['end'] = df['end'].astype(str)
    row = df[df['name'].str.contains(artist)]
    print(row)
    end = row['end'].as_matrix()
    end = [float(number.replace('k', '')) for number in end]
    sales.append(sum(end))

print('-'*50)
print("{} Sold a total of {} units".format(artist, sum(sales)))
