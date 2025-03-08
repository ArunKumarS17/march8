import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_wikipedia_title(browser):
    """Test Wikipedia page title."""
    browser.get("https://www.wikipedia.org")
    assert "Wikipedia" in browser.title

# how to run 
# in terminal navigate to unit folder
# pytest test_example4.py

# Run Tests in Parallel
# pip install pytest-xdist

# install html report
#pip install pytest-html

# pytest filename -n 2 --html=report.html
# -n 2 → Runs tests using 2 parallel workers
# pytest -n 2   (forn entire unittest folder ).
# pytest -n 2 --html=report.html   (for entire unittest folder ).

# Run Specific Tests in Parallel
# pytest filename -n 2 -k "google" --html=report.html
# pytest filename -n 2 -k "wiki" --html=report.html
# pytest -n 2 -k "wiki" --html=report.html   (entire unittest folder)
 
#with out mentioning the filename it will excute all the files in unit folder
# pytest support class and function  
# pytest -n 2 -k "google" --html=report.html