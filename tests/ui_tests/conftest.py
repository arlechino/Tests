import pytest

from ui.main_page import MainPage
from utilities.config_parser import ReadConfig
from utilities.driver_factory import DriverFactory


@pytest.fixture(scope='class')
def create_driver():
    driver = DriverFactory.create_driver(driver_id=ReadConfig.get_driver_id())
    driver.maximize_window()
    driver.get(ReadConfig.get_base_ui_url())
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(create_driver):
    return MainPage(create_driver)

