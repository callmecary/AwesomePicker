import requests
import bs4
import datetime
import json
from yahoo_finance import Share


def get_earning_data(date):
    html = requests.get("https://biz.yahoo.com/research/earncal/{}.html".format(date), headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0"}).text
    soup = bs4.BeautifulSoup(html, "lxml")
    quotes = []
    for tr in soup.find_all("tr"):
        if len(tr.contents) > 3:
            if len(tr.contents[1].contents) > 0:
                if tr.contents[1].contents[0].name == "a":
                    if tr.contents[1].contents[0]["href"].startswith("http://finance.yahoo.com/q?s="):
                        quotes.append({"name": tr.contents[0].text, "symbol": tr.contents[1].contents[0].text, "url": tr.contents[1].contents[0]["href"], "eps": tr.contents[2].text if len(tr.contents) == 6 else u'N/A', "time": tr.contents[3].text if len(tr.contents) == 6 else tr.contents[2].text
                                       })
    return quotes


def get_90days_open_close_stdv(date, symbol):
    end_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = end_date - datetime.timedelta(days=90)
    yahoo = Share(symbol)
    histo_quotes = yahoo.get_historical(str(start_date), date)
    size = len(histo_quotes)
    for histo_quote in histo_quotes:
        histo_quote[""]

    return ""


def getInterestingQuotes(asofdate, previousDt):
    previousQuotes = get_earning_data(previousDt)
    quotes = get_earning_data(asofdate)
    interestingQuotes = []
    for previousQuote in previousQuotes:
        symbol = previousQuote['symbol']
        time = previousQuote['time']
        if time == "After Market Close":
            interestingQuotes.append(previousQuote)
    for quote in quotes:
        symbol = quote['symbol']
        time = quote['time']
        if time == "Before Market Open":
            interestingQuotes.append(quote)
    return interestingQuotes


def main():
    interestingQts = getInterestingQuotes("20161206", "20161205")
    print(interestingQts)

if __name__ == '__main__':
    main()
