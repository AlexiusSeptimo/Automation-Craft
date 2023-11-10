import time

from Pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, "https://demoqa.com/automation-practice-form")
    page.open()
    time.sleep(3)
