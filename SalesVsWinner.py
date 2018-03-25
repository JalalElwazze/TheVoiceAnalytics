import pandas as pd
import matplotlib
matplotlib.use("QT5Agg")
import matplotlib.pyplot as plt

# Open the contestants data
df = pd.read_csv('ArtistSales.csv', encoding="ISO-8859-1")

# List of winners
winners = ['Javier Colon', 'Jermaine Paul', 'Cassadee Pope', 'Danielle Bradbery', 'Tessanne Chin',
           'Josh Kaufman', 'Craig Wayne Boyd', 'Sawyer Fredericks', 'Jordan Smith', 'Alisan Porter',
           'Sundance Head', 'Chris Blue']

# List of runners up
runners = ['Dia Frampton', 'Juliet Simms', 'Terry McDermott', 'Michelle Chamuel', 'Jacquie Lee', 'Jake Worthington',
           'Matt McAndrew', 'Meghan Linsey', 'Emily Ann Roberts', 'Adam Wakefield', 'Billy Gilman', 'Lauren Duski']

# Seasons
season = range(1, 13)

# Sales arrays
w_sales = []
r_sales = []

# Find winner sales
for name in winners:
    row = df[df['Contestant'] == name]
    sale = float(row['Total Sales'].as_matrix())
    w_sales.append(sale)

# Find runner sales
for name in runners:
    row = df[df['Contestant'] == name]
    sale = float(row['Total Sales'].as_matrix())
    r_sales.append(sale)

# Plot
plt.plot(season, w_sales, marker='o', linewidth=0.5)
plt.plot(season, r_sales, marker='o', linewidth=0.5)
plt.xlabel('Season')
plt.ylabel('Sales (Thousands)')
plt.legend(['Winners', 'Runners up'])
plt.show()


