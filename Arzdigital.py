from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from unidecode import unidecode
from math import log, floor


def parse_site(url):
    global Page_soup
    headers = {'User-Agent': 'Mozilla/5.0'}
    Req = Request(url, headers=headers)
    Inspect_code = urlopen(Req)
    Page_soup = BeautifulSoup(Inspect_code, "html.parser")
def number_short_mode(number):
    if number != 0 and not number < 0:
        units = ['', 'K', 'M', 'B', 'T', 'P']
        k = 1000.0
        magnitude = int(floor(log(number, k)))
        return '%.2f%s' % (number / k ** magnitude, units[magnitude])
    else:
        return number
class Get_information:
    def __init__(self, crypto_number):
        self.crypto_number = crypto_number

        self.crypto_html = None
        self.crypto_rank = None
        self.crypto_name_abbreviation = None
        self.crypto_name_complete = None
        self.crypto_price_dollar = None
        self.crypto_price_toman = None
        self.crypto_market_volume = None
        self.crypto_daily_transactions = None
        self.crypto_currency_available = None
        self.crypto_daily_fluctuations = None
        self.crypto_weekly_fluctuations = None

        self.result = ""

        self.def_crypto_rank()
        self.def_crypto_name()
        self.def_crypto_price_dollar()
        self.def_crypto_price_toman()
        self.def_crypto_market_volume()
        self.def_crypto_daily_transactions()
        self.def_crypto_currency_available()
        self.def_crypto_daily_fluctuations()
        self.def_crypto_weekly_fluctuations()
        self.def_result()
        pass

    def def_crypto_rank(self):
        self.crypto_html = Page_soup.find_all("td", {"class": "arz-coin-table-number-td arz-sort-value"})
        self.crypto_rank = str(self.crypto_html[self.crypto_number]["data-sort-value"])
        # print("Rank in the market: " + self.crypto_rank.strip())
        self.result += "\nRank in the market: " + self.crypto_rank.strip()

    def def_crypto_name(self):
        self.crypto_html = Page_soup.find_all("tr", {"class": "arz-coin-tr arz-sort-value-row arz-fiat-parent"})
        self.crypto_name_abbreviation = str(self.crypto_html[self.crypto_number]["data-symbol"])
        self.crypto_name_complete = str(self.crypto_html[self.crypto_number]["data-slug"])
        # print(f"Name: {self.crypto_name_abbreviation.strip()} | {self.crypto_name_complete.strip()}")
        self.result += f"\nName: {self.crypto_name_abbreviation.strip()} | {self.crypto_name_complete.strip()}"

    def def_crypto_price_dollar(self):
        self.crypto_html = Page_soup.find_all("td", {"class": "arz-coin-table-price-td arz-sort-value"})
        self.crypto_price_dollar = str(self.crypto_html[self.crypto_number].text)
        # print("Price(Dollar): " + self.crypto_price_dollar.strip())
        self.result += "\nPrice(Dollar): " + self.crypto_price_dollar.strip()

    def def_crypto_price_toman(self):
        self.crypto_html = Page_soup.find_all("td", {"class": "arz-coin-table-rial-price-td arz-sort-value"})
        self.crypto_price_toman = str(self.crypto_html[self.crypto_number].text)
        self.crypto_price_toman = self.crypto_price_toman.replace("تومان", "")
        self.crypto_price_toman = unidecode(self.crypto_price_toman)
        # print("Price(Toman): " + self.crypto_price_toman.strip())
        self.result += "\nPrice(Toman): " + self.crypto_price_toman.strip()

    def def_crypto_market_volume(self):
        self.crypto_html = Page_soup.find_all("td", {"class": "arz-coin-table-marketcap-td arz-sort-value"})
        self.crypto_market_volume = str(self.crypto_html[self.crypto_number]["data-sort-value"])
        if self.crypto_market_volume.strip() == "":
            # print("Market volume: No information")
            self.result += "\nMarket volume: No information"
        else:
            # print("Market volume: " + str(number_short_mode(float(self.crypto_market_volume.strip()))))
            self.result += "\nMarket volume: " + str(number_short_mode(float(self.crypto_market_volume.strip())))

    def def_crypto_daily_transactions(self):
        self.crypto_html = Page_soup.find_all("td", {"class": "arz-coin-table-volume-td arz-sort-value"})
        self.crypto_daily_transactions = str(self.crypto_html[self.crypto_number]["data-sort-value"])
        if self.crypto_daily_transactions.strip() == "":
            # print("Daily transactions: No information")
            self.result += "\nDaily transactions: No information"
        else:
            # print("Daily transactions: " + str(number_short_mode(float(self.crypto_daily_transactions.strip()))))
            self.result += "\nDaily transactions: " + str(number_short_mode(float(self.crypto_daily_transactions.strip())))

    def def_crypto_currency_available(self):
        self.crypto_html = Page_soup.find_all("td", {"class": "arz-coin-table-circulating-supply-td arz-sort-value"})
        self.crypto_currency_available = str(self.crypto_html[self.crypto_number]["data-sort-value"])
        if self.crypto_currency_available.strip() == "":
            # print("Currency available: No information")
            self.result += "\nCurrency available: No information"
        else:
            # print("Currency available: " + str(number_short_mode(float(self.crypto_currency_available.strip()))))
            self.result += "\nCurrency available: " + str(number_short_mode(float(self.crypto_currency_available.strip())))

    def def_crypto_daily_fluctuations(self):
        self.crypto_html = Page_soup.find_all("td", {"class": "arz-coin-table-daily-swing-td arz-sort-value"})
        self.crypto_daily_fluctuations = str(self.crypto_html[self.crypto_number].text)
        # print("Daily fluctuations: " + self.crypto_daily_fluctuations.strip())
        self.result += "\nDaily fluctuations: " + self.crypto_daily_fluctuations.strip()

    def def_crypto_weekly_fluctuations(self):
        self.crypto_html = Page_soup.find_all("td", {"class": "arz-coin-table-weekly-swing-td arz-sort-value"})
        self.crypto_weekly_fluctuations = str(self.crypto_html[self.crypto_number].text)
        # print("Weekly fluctuations: " + self.crypto_weekly_fluctuations.strip())
        self.result += "\nWeekly fluctuations: " + self.crypto_weekly_fluctuations.strip()

    def def_result(self):
        print(self.result)

for a in range(1):
    parse_site(f"https://arzdigital.com/coins/page-{a}/")
    for i in range(len(Page_soup.find_all("tr", {"class": "arz-coin-tr arz-sort-value-row arz-fiat-parent"}))):
        Get_information(i)
        print("\n\n\n")
