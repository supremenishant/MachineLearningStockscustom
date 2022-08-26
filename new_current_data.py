#from os import lchflags
import requests
from bs4 import BeautifulSoup

headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36',
'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
    'Accept-Language' : 'en-US,en;q=0.5',
    'DNT'             : '1', # Do Not Track Request Header 
    'Connection'      : 'close'}
#url = 'https://www.nseindia.com/get-quotes/equity?symbol=BAJFINANCE'
url='https://finance.yahoo.com/quote/AAPL/key_statistics'
r=requests.get(url,  headers=headers)
print(r.content)