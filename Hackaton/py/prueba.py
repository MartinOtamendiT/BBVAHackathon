from selenium import webdriver
import requests
def create_driver():
    chrome_options =webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:8956")
    driver = webdriver.Chrome(executable_path=r'C:\Users\Guillermo\Downloads\chromedriver_win32\chromedriver.exe', options=chrome_options)
    return driver
def busqueda():
    browser=create_driver()
    print(browser.current_url)
    document.getElementById('button').innerHTML=browser.current_url