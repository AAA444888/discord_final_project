from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

def gg(x):
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    # 设置 WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    # 导航到 Google
    driver.get("https://www.google.com.tw/?hl=zh_TW")
    time.sleep(2)

    # 使用更可靠的选择器找到搜索输入框
    strr='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea'
    search_input = driver.find_element(By.XPATH,strr)
    search_input.send_keys(x)

    # 使用更可靠的选择器找到搜索按钮
    strr='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]'
    search_button = driver.find_element(By.XPATH,strr)
    search_button.click()

    # 等待搜索结果加载
    time.sleep(2)

    # 找到搜索结果中的链接
    search_results = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc")
    i=0
    l=""
    for result in search_results:
        if i==3:
            break
        else:
            link = result.find_element(By.TAG_NAME, "a")
            url = link.get_attribute("href")
            l+=url+"\n"
            i+=1

    # 关闭浏览器
    driver.quit()
    return(l)