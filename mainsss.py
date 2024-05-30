from bs4 import BeautifulSoup
import requests


url = "https://www.booking.com/searchresults.html?ss=" + \
       "Frankfurt%2C+Hessen%2C+Germany" + \
       "&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaDuIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4Aqqi3rI" + \
       "GwAIB0gIkMWYyZGI0YTgtYzg3MC00ZTM0LThiNTUtZWZhODZjNjM5NDU52AIF4AIB&aid=304142&lang=en-us&s" + \
       "b=1&src_elem=sb&src=index&dest_id=-1771148&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=xu" + \
       "&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=54a290950c5c0287&ac_" + \
       "meta=GhAyNjY3OTBhNDM3NDEwM2ExIAAoATICeHU6CUZyYW5rZnVydEAASgBQAA%3D%3D&checkin=2024-06-01&" + \
       "checkout=2024-06-02&" + \
       "group_adults=2&" + \
       "no_rooms=1&" + \
       "group_children=0"

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

html_raw = requests.get(url, headers=headers).text

soup = BeautifulSoup(html_raw, 'lxml')

# Find all the hotel elements in the HTML document
hotels = soup.findAll('div', attrs={'data-testid': 'property-card'})

# Get the Price
# prices = soup.find_all('span', class_='f6431b446c fbfd7c1165 e84eb96b1f')
prices = soup.find_all('span', attrs={'data-testid': 'price-and-discounted-price'})
print(hotels)

