import argparse, time
import urlparse, random , getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup




#utilitis function

def getPeopleLinks(page):  # get the all links of profile of people
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if "profile/view?id=" in url:
                links.append(url)
    return links


def getJobsLinks(page):  # get the all links of jobs
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if "/jobs" in url:
                links.append(url)
    return links

def getLinkID(url):
    p_url = urlparse.urlparse(url)
    #print "P-URL:", p_url
    return urlparse.parse_qs(p_url.query)['id'][0]


def ViewBot(browser):
    visited = {}
    PeopleList = []
    count = 0

    while True:
        time.sleep(random.uniform(1.5,4.2))
        page = BeautifulSoup(browser.page_source)
        people = getPeopleLinks(page)
        if people:
            for p in people:
                ID = getLinkID(p)
                if ID not in visited:
                    PeopleList.append(p)
                    visited[ID] = 1

        if PeopleList:  # if there is people in the list so we look at them
            person = PeopleList.pop()
            browser.get(person)
            count += 1

        else: # find people via jobs
            jobs = getJobsLinks(page)
            if jobs:
                job = random.choice(jobs)
                root = 'http://www.linkedin.com'
                roots = 'https://www.linkedin.com'
                if root not in job or roots not in job:
                    job = "https://www.linkedin.com" + job
                browser.get(job)
            else:
                print "Bot fatal!"
                break

        print "[+] {0} Visited!\n({1}/{2})".format(browser.title, str(count), str(len(PeopleList)))





def Main():
    '''parser = argparse.ArgumentParser()
    parser.add_argument("email", help="linkedin email")
    parser.add_argument("password", help="linkedin password")
    args = parser.parse_args()'''


    email = 'motiga14@gmail.com'#raw_input("enter your LinkedIn email: ")
    password = getpass.getpass("LinkedIn Password: ")

    # set browser

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    browser = webdriver.Chrome(chrome_options=chrome_options)
    print "start browser"
    browser.get("https://www.linkedin.com/uas/login")

    # get email and password fields

    emailElement = browser.find_element_by_id("session_key-login")
    passElement  = browser.find_element_by_id("session_password-login")

    # set email and password

    emailElement.send_keys(email)
    passElement.send_keys(password)
    passElement.submit()

    print "[+] Bot Success to Login...START"


    ViewBot(browser)
    browser.close()






if __name__ == "__main__":
    Main()
















