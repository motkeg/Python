
import datetime, urllib
from selenium import webdriver
from bs4 import BeautifulSoup





def GetInfo(browser, symbol,):
    print "retriving data..." + str(datetime.datetime.now())

    page = BeautifulSoup(browser.page_source)
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if "/table.csv" in url:
                csv = urllib.URLopener()
                csv.retrieve(url, "downloads/data_"+symbol+".csv")

                print "URL: ", url

                print "Download complate! check 'downloads' directory"
                return url




def Main(q=False):
    symbol = raw_input("{be sure you know the specific name of the stock}\n" +
                              "enter favorite SYMBOL:" )
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    browser = webdriver.Chrome(chrome_options=chrome_options)
    print "start browser"

    url = "http://finance.yahoo.com/quote/" +symbol +"/history?period1=1315688400&period2=1473541200&interval=1d&filter=history&frequency=1d"
    browser.get(url)

    GetInfo(browser, symbol)

    browser.close()



if __name__ == "__main__":
    Main()