# All below three imports for method test_google_search_using_manager
from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



# test using fixture and default chrom driver location
def test_google_title(browser):
    browser.get("https://www.google.com/")
    assert "Google" in browser.title


# test using chrome driver manager to install latest driver every time
def test_google_search_using_manager():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    print(driver.title)  # Should print Google page title
    driver.quit()


def test_google_search(browser):
    browser.get("https://www.google.com/")
    searchbox = browser.find_element(By.NAME, "q")
    searchbox.send_keys("Selenium PyTest")
    searchbox.submit()

    print(browser.title)


