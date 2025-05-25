import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestMainPage():

    def test_add_to_busket_button(self, browser):
        # ожидание для поиска элементов
        browser.implicitly_wait(5)

        browser.get(link)

        # проверка наличия кнопки
        buttons_list = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
        time.sleep(10)
        assert len(buttons_list) > 0, 'button not found'