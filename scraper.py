from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

def scrape_news(keyword):
    options = Options()
    
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    try: 
        url = f"https://timkiem.vnexpress.net/?q={keyword}"
        driver.get(url)
    
    #time.sleep(2)
    
        WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME,'title-news'))
        )
    
    
        page_source = driver.page_source
        soup = BeautifulSoup(driver.page_source,'html.parser')
        driver.quit()
    
        
        
        articles = soup.select('h3.title-news a')
        
        results = []
        for a_tag in articles:
            title = a_tag.get_text(strip=True)
            link = a_tag['href']
            if not link.startswith('http'):
                link = 'http://vnexpress.net' + link
            results.append({'title':title,'link':link})
            
        print("Tìm được:",len(results),"bài.")
        return results
    except Exception as e:
        print("Lỗi xảy a:",e)
        return []
    
    finally:
        driver.quit()