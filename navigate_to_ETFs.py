from selenium import webdriver
import locators
import scraper

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://finance.yahoo.com/')

actions = ActionChains(driver)

sector_tab = driver.find_element(By.XPATH, locators.sector_tab)
actions.move_to_element(sector_tab).perform()

technology_subtab = driver.find_element(By.XPATH, locators.sector_tab_technology)
technology_subtab.click()

wait = WebDriverWait(driver, 10)
technology_section_header = wait.until(
      expected_conditions.visibility_of_element_located((By.XPATH, locators.technology_section_header)))
actions.scroll_to_element(
      driver.find_element(By.XPATH, locators.etf_opportunities_header)
).perform()

view_more = driver.find_element(By.XPATH, locators.etf_opportunities_view_more)
if view_more.is_displayed():
      view_more.click()
      etfs_header = wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.top_etfs_header)))
      results_table = driver.find_element(By.ID, locators.results_table)
      actions.scroll_to_element(results_table).perform()
      scraper.scrape_etf_data(driver)
      
      

