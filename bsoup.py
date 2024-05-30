from bs4 import BeautifulSoup
import requests
import pandas as pd

from assets.citycode import city_code

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}


# Scrape hotel data
# Will return pandas dataframe
def get_hotel_data(city, checkin, checkout):
    url = ("https://www.booking.com/searchresults.html?ss=" +
           city +
           "&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaDuIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4Aqqi3rI" +
           "GwAIB0gIkMWYyZGI0YTgtYzg3MC00ZTM0LThiNTUtZWZhODZjNjM5NDU52AIF4AIB&aid=304142&lang=en-us&s" +
           "b=1&src_elem=sb&src=index&" +
           "dest_id=-"+ str(city_code[city]) +
           "&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=xu" +
           "&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=54a290950c5c0287&ac_" +
           "meta=GhAyNjY3OTBhNDM3NDEwM2ExIAAoATICeHU6CUZyYW5rZnVydEAASgBQAA%3D%3D" +
           "&checkin=" + checkin + '&' +
           "checkout=" + checkout + '&' +
           "group_adults=2&" +
           "no_rooms=1&" +
           "group_children=0")
    html_raw = requests.get(url, headers=headers).text

    soup = BeautifulSoup(html_raw, 'lxml')

    # Find all the hotel elements in the HTML document
    hotels_raw = soup.findAll('div', attrs={'data-testid': 'property-card'})

    hotels = []

    for hotel in hotels_raw:
        # Extract the hotel name
        name_element = hotel.find('div', {'data-testid': 'title'})
        name = name_element.text.strip()

        # Extract the hotel location
        location_element = hotel.find('span', {'data-testid': 'address'})
        location = location_element.text.strip()

        # Extract the hotel price
        price_element = hotel.find('span', {'data-testid': 'price-and-discounted-price'})
        price_full = price_element.text.strip().split()
        price = price_full[1]
        currency = price_full[0]

        # Extract the hotel rating
        rating_element = hotel.find('div', {'data-testid': 'review-score'})
        rating = rating_element.text[:3]

        #Append hotes_data with info about hotel
        hotels.append({
            'name': name,
            'location': location,
            'price': float(price),
            'currency': currency,
            'rating': rating
        })

    return pd.DataFrame(hotels)


