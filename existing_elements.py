from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest


class ExistsElement(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://google.com')    # Link to resourse

    def existing_element(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath('xpath')    # element's xpath
        except NoSuchElementException:
            return False
        return True

    def test_search_result(self):
        self.assertTrue(existing_element('xpath'))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
