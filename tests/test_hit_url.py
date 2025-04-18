import pytest

import config
from pages.login_page import LoginPage


def test_hit_url(driver,wait):
    login_page = LoginPage(driver,wait)
    driver.get(config.LINKEDIN_URL)
    assert 'LinkedIn' in driver.title
    assert config.LINKEDIN_URL == driver.current_url
    login_page.enter_username()
    login_page.enter_password()
    login_page.submit()
    assert 'Feed' in driver.title



