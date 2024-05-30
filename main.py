from datetime import datetime, timedelta

from bsoup import get_hotel_data

# Sets the from and to date, in which the data are being imported
start_date = datetime(2024, 7, 1)
end_date = datetime(2024, 7, 10)

# Collects the scraped data and outs into csv.
# Contains hotel dataframe and date
hotels_dataframes = []

# Iterate through each day in the timeframe and collect the data
current_date = start_date
while current_date < end_date:
    # Using beautifulsoup scrape data
    current_date_str = current_date.strftime('%Y-%m-%d')

    hotels_pd = get_hotel_data(
        'Frankfurt_Hessen_Germany',
        current_date_str,  # Current date
        (current_date + timedelta(days=1)).strftime("%Y-%m-%d")  # Current date + 1
    )
    hotels_dataframes.append(
        {
            'pd': hotels_pd,
            'checkin_date': current_date_str
        }
    )
    print(f"===== Data on {current_date_str} scraped! =====")

    current_date += timedelta(days=1)

# Exports all scraped data to separate csv
for hotels in hotels_dataframes:
    filename = hotels['checkin_date'] + '.csv'
    # Sorts the hotels by name and export them
    hotels['pd'].sort_values(by=['name'], ascending=True).to_csv('output/' + filename, sep=';', header=True,
                                                                 index=False)

# Get length of dataframe
# length = len(hotels_pd.index)
# print(length)
