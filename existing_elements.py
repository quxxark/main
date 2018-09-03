from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest


class ExistsElement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://google.com')    # Link to resourse

    def test_existing_test(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath('xpath')    # element's xpath
        except NoSuchElementException:
            return False
        return True
# self.assertTrue(check_exists_by_xpath(xpath))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
