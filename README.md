
# Travel-Scrape: Collecting Hotel Booking data from booking.com

Hello! I am creating a simple project to deepen my understanding in python and data science. The extrated data would then processed with pandas library, and then saved as an csv file.




## Objectives

    1. Understanding web scraping using various tools.
    2. Trying to parse HTML data in order to get various informations.
## Tools and Technologies

    Python 3.8
    BeautifulSoup, for parsing HTML and extracting data.
    Requests, to handle HTTP requests.
    Pandas, for data manipulation.
    Matplotlib and seaborn, for visualization from data.
## Features 

    1. Data-scraping with BeautifulSoup, given start time and end time. This program would look for hotel bookings for one night for each day in this time period. The scraped data are:
        a. Date in which the data is scraped
        b. Name of hotel
        c. Location
        d. Hotel rating
        e. Price

    2. Outputs the data to a csv file for each day.
    3. Collecting and merging the data using pandas, while also processing data from them such as min, max, and mean.
    4. (TODO) Visualizes the result.
## Next step

The next step of this project would be using other scraping libraries such as Selenium, as some of the results are locked behind user's action such as scrolling down.

Using another website as a price comparison would also be good, as from my own experience, the prices from different websites varies, even though I was using the same search queries for the same date.

Creating an API could also be an option, such that this program could be accessed easily without installing python environment.