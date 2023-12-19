from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from firebase import firebase
from selenium.webdriver.chrome.options import Options

def ytv(x):
    url = 'https://cooldiscordbot-60404-default-rtdb.firebaseio.com/'
    fdb = firebase.FirebaseApplication(url, None)
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get("https://www.youtube.com/results?search_query="+x)
    time.sleep(2)
    s1='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a'
    s2='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]/div[1]/div/div[1]/div/h3/a'
    s3='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[3]/div[1]/div/div[1]/div/h3/a'
    link = driver.find_element(By.XPATH,s1)
    p="[1]"+link.get_attribute('title')+"\n"
    fdb.put('/','v1',link.get_attribute('href'))
    link = driver.find_element(By.XPATH,s2)
    p+="[2]"+link.get_attribute('title')+"\n"
    fdb.put('/','v2',link.get_attribute('href'))
    link = driver.find_element(By.XPATH,s3)
    p+="[3]"+link.get_attribute('title')
    fdb.put('/','v3',link.get_attribute('href'))
    driver.quit()
    return(p)