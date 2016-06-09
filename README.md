# JobLeadGenerator
A Python 3.4 app that generates job leads

Requirements: 
python3.4,
beautifulsoup4,
wxPython phoenix,

This app currently scrapes the software job posting in craigslist. 
Once it finds the job listing it presents the job posting in a new tab on your web browser.
It can scrape the posting for job title
    (soon to include company and hiring manager) if acceptable.
It can fill in a pre set cover letter with scraped infomation.
It can save the job info that was provided and will not genereate the same lead multiple times.

Soon to come:
Generating from different sources on craigslist and even other web sites.
Generating job leads from specific key words.
Taking you to the apply online location if present.
auto emailing coverletter and resume to job posting.
filling a google spreadsheet with database information.
easier installation process
easier run process

Installation:

For Python3.4:
    https://www.python.org/downloads/release/python-344/
    
For Beautifulsoup4:
    Make sure pip is up to date,
    use command prompt:
    
        cd C:\Python34\Scripts (or equiviland path)
        pip install --upgrade pip
        pip install beautifulsoup4

For WxPython Phoenix:
    Make sure pip is up to date,
    use command prompt:
    
        cd C:\Python34\Scripts (or equiviland path)
        pip install --upgrade pip
        pip install -U --pre --trusted-hoast \
        wxpython.org -f http://wxpython.org/Phoenix/snapshot-builds/ \
        wxPython_Phoenix==3.0.3.dev2054+14a1ddd-cp27-cp27m-win_amd64 (or equivilant build)
            
To find what build best fist your platform go to http://wxpython.org/Phoenix/snapshot-builds/
find your build and replace the example build with your prefered build.
Example:
My build was:
    
        wxPython_Phoenix-3.0.3.dev2054+14a1ddd-cp27-cp27m-win_amd64.whl
        
Change this to:
    
        wxPython_Phoenix==3.0.3.dev2054+14a1ddd-cp27-cp27m-win_amd64
        
And add this to the command prompt as:
        
        pip install -U --pre --trusted-hoast \
        wxpython.org -f http://wxpython.org/Phoenix/snapshot-builds/ \
        wxPython_Phoenix==3.0.3.dev2054+14a1ddd-cp27-cp27m-win_amd64

For JobLeadGenerator:

Download .zip,
Unpack .zip,
Open from Python3.4 (GUI),
press F5 to run
