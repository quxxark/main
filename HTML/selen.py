from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s'
)


class GoogleSearch(unittest.TestCase):
    def setUp(self):  # Precondition. Это едйствие будет запускаться вначале каждого теста
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('chromedriver', options=self.options)
        self.driver.get('https://google.com')  # Вначале каждого теста открывать страницу

    def test_01(self):
        driver = self.driver
        input_field = driver.find_element_by_id('lst-ib')  # Ищем поле ввода по ID (dev tools)
        input_field.send_keys('python')  # Данные, которые хотим передать в поле ввода
        input_field.send_keys(Keys.ENTER)  # Имитация нажатия клавиши

        time.sleep(2)  # Ждём 2 секунды

        titles = driver.find_elements_by_class_name('r')  # Список всех тайтлов поисковых результатов с <h3 class="r">
        for title in titles:
            assert 'python' in title.text.lower()  # УТВЕРЖДАЕМ, что слово 'python' есть во всех тайтлах

    def test_02(self):
        driver = self.driver
        input_field = driver.find_element_by_id('lst-ib')
        input_field.send_keys('python')

        time.sleep(2)

        input_field.send_keys(Keys.ARROW_DOWN)
        input_field.send_keys(Keys.ARROW_DOWN)
        input_field.send_keys(Keys.ENTER)

        titles = driver.find_elements_by_class_name('r')  # Список всех тайтлов поисковых результатов с <h3 class="r">
        for title in titles:
            assert 'python' in title.text.lower()  # УТВЕРЖДАЕМ, что слово 'python' есть во всех тайтлах

    def tearDown(self):  # Post-conditions. Метод вызывается ПОСЛЕ прохождения каждого тесткейса
        self.driver.quit()  # Закрыть браузер


if __name__ == '__main__':
    unittest.main()
