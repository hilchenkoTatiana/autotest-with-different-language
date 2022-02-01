import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_present_button_the_card(browser):
    browser.get(link)
    button_is_present = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form button")
    time.sleep(2)
    assert expected_conditions.element_to_be_clickable(button_is_present)
