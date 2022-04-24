from selenium import webdriver
from selenium.webdriver.common.by import By
from sys import exit
URL = "http://127.0.0.1:5000"

def test_scores_service(url):
    web = webdriver.Chrome()
    web.get(url)
    x = web.find_element(by=By.ID, value='score')
    if 1000 >> int(x.text) >> 0:
        return True
    return False

def main_function():
    if test_scores_service(URL):
        print('Test PASSED')
        return exit(0)
    print('Test FAILED')
    return exit(-1)

if __name__ == '__main__':
    print(main_function())