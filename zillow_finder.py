import bs4
import requests


ZILLOW_WEBPAGE = "https://www.zillow.com/manhattan-new-york-ny/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Manhattan%2C%20New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.05066245825195%2C%22east%22%3A-73.9157366159668%2C%22south%22%3A40.71484440927905%2C%22north%22%3A40.79122913614269%7D%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12530%2C%22regionType%22%3A17%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A583600%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A2000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

REQUEST_HEADINGS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6",
}

class zillow_finder():
    def __init__(self):
        self.pages_to_scrape = 3

    def get_zillow_data(self):
        response = requests.get(url=ZILLOW_WEBPAGE, headers=REQUEST_HEADINGS)
        zillow_text = response.text

        soup = bs4.BeautifulSoup(zillow_text, "html.parser")
        zillow_links = soup.find_all(class_="list-card-link list-card-link-top-margin")
        zillow_prices = soup.find_all(class_="list-card-price")
        zillow_address = soup.find_all(class_="list-card-addr")

        links_list = []

        for link in zillow_links:
            url = link.get("href")
            if url[0] == "/":
                links_list.append(f"https://www.zillow.com{url}")
            else:
                links_list.append(url)

        prices_list = []
        for price in zillow_prices:
            prices_list.append(price.text[1:6])

        address_list = []
        for address in zillow_address:
            address_list.append(address.text)

        print([links_list, prices_list, address_list])

        return [links_list, prices_list, address_list]