# Python program to scrape website
# and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv


def main(url, search_term):

    r = requests.get(url)
    # print(r.content)

    soup = BeautifulSoup(r.content, "html5lib")
    print(soup)

    quotes = []  # a list to store quotes

    table = soup.findAll("a", attrs={"class": "text-small"})
    print(table)

    # for row in table.findAll("div", attrs={"class": "quote"}):
    #     print(row)
    #     quote = {}
    #     quote["theme"] = row.h5.text
    #     quote["url"] = row.a["href"]
    #     quote["img"] = row.img["src"]
    #     quote["lines"] = row.h6.text
    #     quote["author"] = row.p.text
    #     quotes.append(quote)

    # filename = "inspirational_quotes.csv"
    # with open(filename, "wb") as f:
    #     w = csv.DictWriter(f, ["theme", "url", "img", "lines", "author"])
    #     w.writeheader()
    #     for quote in quotes:
    #         w.writerow(quote)


if __name__ == "__main__":
    url = "https://www.google.com/imghp?hl=en"
    search_term = "ash tree fall"
    main(url, search_term)
