from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import random

MAX_TIMEOUT = 25 # change timeout duration

def load_proxies(PATH): # for loading the proxies
    return open(PATH).read().split('\n') 

def load_session(url,proxy):
    proxy,port = proxy.split(':')
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", proxy)
    profile.set_preference("network.proxy.http_port", port)
    profile.set_preference("network.proxy.ssl", proxy)
    profile.set_preference("network.proxy.ssl_port", port)
    profile.update_preferences()

    driver = webdriver.Firefox(firefox_profile=profile)
    driver.set_page_load_timeout(10)
    driver.get(url)

  
    time.sleep(MAX_TIMEOUT)
    driver.quit()



def main(url):
    proxies = load_proxies("proxies.txt")
    c=1
    while True:
        id = random.randrange(0,len(proxies))
        proxy = proxies[id]
        try:
            load_session(url,proxy)
            print("View counted:",c)
            c+=1
        except Exception as e:
            print("Skipping as excepted:",str(e))

        
if __name__ == "__main__":
    main(input("Enter URL:"))