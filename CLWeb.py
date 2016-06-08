##A web scraper that gets the contents of any graigslist post
##
##
##
##
##

import re, db_program
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Get the html layout of the page
def scrapePage(webPath):
    #Check if page exists
    try:
        # Open webpage
        webpage = urlopen(webPath)

        # Convert to BeautifulSoup
        soup = BeautifulSoup(webpage, "html.parser")
        return soup
    except:
        return "WebPage Not found"


#Finds the position of the posting
def findPosition(webPath):
    #try to find position
    try:
        soup = scrapePage(webPath)
        #finds a specific identifier
        cursor = soup.find(id="titletextonly")
        position = cursor.get_text()
        return position
    except:
        return "/Position not found"
    
#Find the postID
def findPostID(webPath):
    #try to find postID
    try:
        soup = scrapePage(webPath)
        #find a pecific identifier
        cursor = soup.findAll("p", text= re.compile("post id") )
        for ID in cursor:
            postID = ID.get_text()
            postID = postID.replace("post id: ", "")
        return postID
    except:
        return "postID not found" 

#Find posing body (pBody)
def findPBody(webPath):
    #try to find pBody or the contents of the job posting
    try:
        soup = scrapePage(webPath)
        #Get div id posing body
        cursor = soup.find(id="postingbody")
        pBody = cursor.get_text()
        return pBody
    except:
        return "/pBody not found"

#Check database for website
def checkDb(weblink):
    results = db_program.QueryDb("Website", "Website", weblink)
    #check for results
    #if any result then is equal is true
    if(results != []):
        isEqual = True
    #if no results then is equal is false
    else:
        isEqual = False

    return isEqual

#Get the posting http address
def getAddress():
    searchPage = "https://portland.craigslist.org/search/sof"
    soup = scrapePage(searchPage)
    linkList = soup.findAll("a", {"class":"hdrlnk"})
    for link in linkList:
        
        webLink = "https://portland.craigslist.org" + link['href']
        #check if already in database
        inDatabase = checkDb(webLink)
        #if in databse go to next
        if (inDatabase == True):
            pass
        #if not send to program
        else:
            break
        
    return webLink









    

 
