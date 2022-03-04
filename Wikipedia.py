from bs4 import BeautifulSoup
from urllib.request import urlopen

Language = input("English(e) or persian(p): ")

if Language == "e":
    Search = input("Search: ")
    Url = "https://en.wikipedia.org/wiki/" + Search
elif Language == "p":
    def text_encode(text):
        Text = text
        Text = Text.replace(" ", "_")
        Text = str(Text.encode())
        Text = Text[2:-1]
        Text = Text.replace("\\x", "%").upper()
        return Text

    Url = "https://fa.wikipedia.org/wiki/" + text_encode(input("Search: "))

try:
    req = urlopen(Url)
    page_html = req.read()
    req.close()

    page_soup = BeautifulSoup(page_html, "html.parser")


    class class_get_information:
        def __init__(self):
            self.information = None
            self.Text = None

            self.def_main_information()

        def def_main_information(self):
            self.information = page_soup.find_all("p")
            self.Text = ""
            for i in self.information[0:10]:
                self.Text += i.text
            for i in self.Text:
                if i == "[":
                    x = self.Text.index(i)
                    self.Text = self.Text.replace(self.Text[x:self.Text.index("]") + 1], "", 1)
            self.Text = self.Text.replace(" ", " ")
            Result = self.Text
            print(Result)

    class_get_information()
except:
    if Language == "e":
        print("oops nothing found!")
    else:
        print("آخ آخ چیزی پیدا نشد!")

input("\nPress enter to exit...")
