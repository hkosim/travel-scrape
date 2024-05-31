import os
from datetime import datetime, timedelta

import pandas as pd

# Sets the from and to date, in which the data are being imported
start_date = datetime(2024, 7, 1)
end_date = datetime(2024, 7, 31)

label_date_list = []
df_merged = pd.DataFrame(columns=['name', 'rating'])

# Load all scraped data
current_date = start_date
while current_date < end_date:
    current_date_str = current_date.strftime('%Y-%m-%d')
    label_date_list.append('price_'+current_date_str)

    # Defines the path of current and try to read the data
    path_df_curr = os.path.join('output', current_date_str + '.csv')
    # path_df_next = os.path.join('output', (current_date + timedelta(days=1)).strftime('%Y-%m-%d') + '.csv')
    try:
        df_curr = pd.read_csv(path_df_curr, sep=';')
        # df_next = pd.read_csv(path_df_next)

    except FileNotFoundError:
        print(f"The file '{path_df_curr}' does not exist.")
    except Exception as e:
        # Catch all other exceptions
        print(f"An error occurred while reading the file: {e}")

    # Renaming the price column to current_date_str
    df_curr.rename(columns={'price': 'price_'+current_date_str}, inplace=True)

    # Perform an outer merge to see the prices of all scraped hotels
    df_merged = pd.merge(df_merged, df_curr[['name', 'rating', 'price_'+current_date_str]], on=['name', 'rating'], how='outer')

    current_date += timedelta(days=1)

# Creates new columns: count, min, max, average
df_merged['count'] = df_merged.count(axis=1)-1
df_merged['min'] = df_merged[label_date_list].min(axis=1)
df_merged['max'] = df_merged[label_date_list].max(axis=1)
df_merged['average'] = df_merged[label_date_list].mean(axis=1).round(3)

# Exports the data
df_merged[df_merged['count'] > 10].sort_values(by=['rating'], ascending=False).to_csv('output/' + 'merged_price.csv', sep=';', header=True,
                                                                     index=False)
print("File exported successfully.")




