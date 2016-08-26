##Write a script that checks 100 pages asyncrously
##Next steps:
##Write a module that saves the pages to a database
##check the database for scanned pages before rescanning pages
##write a module that chooses the best JP from database to present to user
##
##



import re, db_program
from urllib.request import urlopen
from bs4 import BeautifulSoup
from CLWeb import ScrapePage
from time import time
from time import sleep
from threading import Thread
from multiprocessing.pool import ThreadPool
from LogExecutionTime import logExecutionTime

def getLinkList():
    searchPage = "https://portland.craigslist.org/search/sof"
    page = ScrapePage(searchPage)
    soup = page.soup
    linkList = soup.findAll("a", {"class":"hdrlnk"})
    return linkList

def timedScrape(webPath,pageList,i):
    TimedScrape = logExecutionTime(ScrapePage)
    returnValue = TimedScrape(webPath)
    print(returnValue)
    pageList[i] = returnValue
    return returnValue
    
def main(linkList):
    # Starting as a daemon means
    # the thread will not prevent the process from exiting.
    pageList = [None] * len(linkList)
    threads = [None] * len(linkList)
    
    #print ("pageList: " +len(pageList))
    #print ("threads: " + len(threads))
    print ("linkList: "+ str(len(linkList)))
    for i in range(len(linkList)):
        link = linkList[i]
        webPath = "https://portland.craigslist.org{}".format(link['href'])
        print(webPath)
        try:
            print("Trying...")
            threads[i] = Thread(target=timedScrape, args=(webPath,pageList, i))
            
            threads[i].start()
        except:
            print("Failed!")
            pass
        
    for i in range(len(threads)):
        threads[i].join()
        
    return pageList


timedGetLinkList = logExecutionTime(getLinkList)
linkList = timedGetLinkList()
threads = main(linkList)


