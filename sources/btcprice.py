# importing libraries
from bs4 import BeautifulSoup as BS
import requests, time


from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
bot = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

def scrolling(url):
    bot.get(url)
    
    #waiting for the page to load
    time.sleep(1) 
    #repeat scrolling 10 times

    return more_scroll()
def more_scroll():
    for i in range(2):
        #scroll 300 px
        bot.execute_script('window.scrollTo(0,(window.pageYOffset+3000))')
        #waiting for the page to load
        time.sleep(1) 
    html=bot.execute_script("return document.body.innerHTML;")
   
    return html


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
# method to get the price of bit coin
def get_price(url):
	
	# getting the request from url
	#data = requests.get(url, headers=headers).text
	data=scrolling(url)
	print(data)
	i=data.find("eur")
	#ans=data[i-500:i+500]
	return data

# url of the bit coin price
#url = "https://www.google.com/search?q=bitcoin+price"

# calling the get_price method
#ans = get_price(url)

# printing the ans
#print(ans)
while 1:
	url = "https://www.google.com/search?q=bitcoin+price"
	print(get_price(url))
	time.sleep(2)
