from time import sleep
from chromote import Chromote

chrome = Chromote()
tab = chrome.tabs[0]

sites = [
    'https://github.com',
    'http://stackoverflow.com',
]

while True:
    for site in sites:
        tab.set_url(site)
        sleep(30)