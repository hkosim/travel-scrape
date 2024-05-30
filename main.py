from bsoup import get_hotel_data

# TESTING BEAUTIFULSOUP
hotels_pd = get_hotel_data(
    'Frankfurt Hessen Germany',
    '2024-06-01',
    '2024-06-02'
)

hotels_pd_2 = get_hotel_data(
    'Berlin',
    '2024-06-02',
    '2024-06-03'
)

print(hotels_pd.sort_values(by=['price'], ascending=True).head())
print(hotels_pd_2.sort_values(by=['price'], ascending=True).head())

# Get length of dataframe
# length = len(hotels_pd.index)
# print(length)