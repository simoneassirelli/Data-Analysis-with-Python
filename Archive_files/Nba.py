import pandas as pd

#                               *DATA INSPECTION*

df_nba = pd.read_csv("NBA_Finals.csv", sep=";")
print(df_nba.head())
# Change "MVP Height (m)" column name
df_nba = df_nba.rename(columns={'MVP Height (m)' : 'MVP Height m'})
# What are the columns of this dataset?
print(df_nba.columns)
# How many players are there in the dataset?
num_players = len(df_nba)
print("\nNumber of players in the dataset: ", num_players, "\n")
# Let's check for missing values
missing_values = df_nba.isna().sum() #.isnull is the same
print("\nMissing Values:\n", missing_values)


#                               *DATA ANALYSIS*

# What is the average age of the players?
player_age = 2023 - df_nba["Year"]
average_age = player_age.mean()
print(average_age)
# Add "player_age" column to dataset
df_nba["Player age"] = player_age
print(df_nba.columns)
print(df_nba.head())
# Now let's look at some statistics about the data
print("\nStatistics:\n")
print(df_nba.describe())
# How many times has Lebron won MVP Finals
lebron_mvp = df_nba[df_nba['MVP Name'] == "L. James"][["Year", "NBA Champion", "MVP Name", "Player age"]]
print(lebron_mvp)
lebron_count = lebron_mvp["MVP Name"].value_counts()
print(lebron_count)

df_nba.to_csv("Nba_to_adjust.csv")









# I want to know who won the NBA in 2016
print(df_nba[df_nba["Year"] == 2016]["NBA Champion"])
# Who was the mvp?
print(df_nba[df_nba["Year"] == 2016]["MVP Name"])


# Create a pivot table
# pivot_table = pd.pivot_table(df_nba, index= 'MVP name', values = 'MVP Height (m)')

