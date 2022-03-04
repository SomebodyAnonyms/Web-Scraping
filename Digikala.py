from bs4 import BeautifulSoup
from urllib.request import urlopen as UrlReq
from unidecode import unidecode


Url = "https://www.digikala.com/search/?q=" + input("Search: ")  # Search

client = UrlReq(Url)
Page_html = client.read()
client.close()

Page_soup = BeautifulSoup(Page_html, "html.parser")

class Get_products_information:
    def __init__(self, Product_Number):
        self.Product_Number = Product_Number
        self.Products_html = None
        self.Product = None
        self.Product_name = None
        self.Product_price = None
        self.Product_Rate = None
        self.Product_Votes = None
        self.Product_Seller = None
        self.Product_Status = None
        self.Product_name_count = None
        self.Product_price_count = None
        self.Product_Rate_count = None
        self.Product_Votes_count = None
        self.Product_Seller_count = None
        self.Product_Status_count = None
        self.def_Product_name()
        self.def_Product_Price()
        self.def_Product_Rate_and_Vote()
        self.def_Product_Seller()
        self.def_Product_Status()

    def def_Product_name(self):
        self.Products_html = Page_soup.find_all("div", {"class": "c-product-box__title"})
        self.Product_name_count = len(self.Products_html)
        if self.Product_Number > self.Product_name_count - 1:
            print("Name: " + "No information")
        else:
            self.Product = self.Products_html[self.Product_Number]
            self.Product_name = str(self.Product.a.text)
            print("Name: " + self.Product_name.strip())

    def def_Product_Price(self):
        self.Products_html = Page_soup.find_all("div", {"class": "c-price__value-wrapper"})
        self.Product_price_count = len(self.Products_html)
        if self.Product_Number > self.Product_price_count - 1:
            print("Price: " + "No information")
        else:
            self.Product = self.Products_html[self.Product_Number]
            self.Product_price = str(self.Product.text)
            self.Product_price = self.Product_price.replace("تومان", "")
            self.Product_price = unidecode(self.Product_price)
            print("Price: " + self.Product_price.strip() + " Toman")

    def def_Product_Rate_and_Vote(self):
        self.Products_html = Page_soup.find_all("div", {"class": "c-product-box__engagement-rating"})
        self.Product_Rate_count = len(self.Products_html)
        if self.Product_Number > self.Product_Rate_count - 1:
            print("Rate: " + "No information")
        else:
            self.Product = self.Products_html[self.Product_Number]
            self.Product_Rate, self.Product_Votes = str(self.Product.text), str(self.Product.text)
            self.Product_Rate, self.Product_Votes = unidecode(self.Product_Rate), unidecode(self.Product_Votes)
            self.Product_Rate, self.Product_Votes = self.Product_Rate.replace("\n", ""), self.Product_Votes.replace("\n", "")
            self.Product_Rate, self.Product_Votes = self.Product_Rate.replace(" ", ""), self.Product_Votes.replace(" ", "")
            self.Product_Rate, self.Product_Votes = self.Product_Rate[0:3], self.Product_Votes[3:]
            self.Product_Votes = self.Product_Votes.replace("(", "")
            self.Product_Votes = self.Product_Votes.replace(")", "")
            print("Rate: " + self.Product_Rate.strip() + "  -  " + self.Product_Votes.strip() + " person voted")
        
    def def_Product_Seller(self):
        self.Products_html = Page_soup.find_all("div", {"class": "c-product__seller-details c-product__seller-details--item-grid"})
        self.Product_Seller_count = len(self.Products_html)
        if self.Product_Number > self.Product_Seller_count - 1:
            print("Seller: " + "No information")
        else:
            self.Product = self.Products_html[self.Product_Number]
            self.Product_Seller = str(self.Product.text)
            if "برگزیده" in self.Product_Seller:
                self.Product_Seller = self.Product_Seller.replace("فروشنده:", "")
                self.Product_Seller = self.Product_Seller.replace("برگزیده", "")
                self.Product_Seller = self.Product_Seller.replace("\n", "")
                print("Seller: " + self.Product_Seller.strip() + " *****")
            else:
                self.Product_Seller = self.Product_Seller.replace("فروشنده:", "")
                self.Product_Seller = self.Product_Seller.replace("\n", "")
                print("Seller: " + self.Product_Seller.strip())

    def def_Product_Status(self):
        self.Products_html = Page_soup.find_all("div", {"class": "c-product-box__status"})
        self.Product_Status_count = len(self.Products_html)
        if self.Product_Number > self.Product_Status_count - 1:
            print("Status: " + "No information")
        else:
            self.Product = self.Products_html[self.Product_Number]
            self.Product_Status = str(self.Product.text)
            self.Product_Status = self.Product_Status.replace("\n", "")
            self.Product_Status = self.Product_Status.replace("                            ", " ")
            print("Status: " + self.Product_Status.strip())

for i in range(len(Page_soup.find_all("div", {"class": "c-product-box__engagement-rating"}))):
    Get_products_information(i)
    print("\n\n")

input("\nPress enter to exit...")

