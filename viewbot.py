from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import random
import threading

MAX_TIMEOUT = 25 # change timeout duration
THREAD_COUNT = 1 # change no. of instances of threads to open at once
c=1 # keep track of counts

def load_proxies(PATH): # for loading the proxies
    return open(PATH).read().split('\n') 

def load_session(url,proxy): # manage each session
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
    try:
        driver.get(url)
        time.sleep(MAX_TIMEOUT)
        driver.quit()
    except:
        driver.quit()
        raise Exception("Failed to load website")


def main(url):
    global c
    proxies = load_proxies("proxies.txt")
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
    url = input("Enter url:")
    threads = []
    for i in range(THREAD_COUNT):
        thread = threading.Thread(target=main,args=(url,))
        threads.append(thread)
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
     


    
