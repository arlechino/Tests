from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, time_to_wait: int = 5):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, time_to_wait)

    def _navigation_back(self):
        self._driver.back()

    def _wait_until_element_visible(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def _wait_until_element_located(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def _wait_until_element_clickable(self, locator):
        return self._wait.until(EC.element_to_be_clickable(locator))

    def _is_disappeared(self, locator):
        try:
            self._wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def _scroll_to_element_by_js(self, locator):
        element = self._wait_until_element_visible(locator)
        self._driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def _click_by_js(self, locator):
        element = self._wait_until_element_located(locator)
        self._driver.execute_script("arguments[0].click();", element)

    def _send_keys(self, locator, value, is_clear=True):
        element = self._wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def _click(self, locator):
        self._wait_until_element_clickable(locator).click()

    def _is_displayed(self, locator):
        try:
            self._wait_until_element_visible(locator)
            return True
        except TimeoutException:
            return False

    def is_url_contain(self, url: str):
        return self._wait.until(EC.url_contains(url))

    def _get_attribute_value(self, locator, attribute_name) -> str:
        element = self._wait_until_element_located(locator)
        return element.get_attribute(attribute_name)

    def _get_text(self, locator) -> str:
        element = self._wait_until_element_visible(locator)
        return element.text

    def _is_enabled(self, locator) -> bool:
        element = self._wait_until_element_located(locator)
        return element.is_enabled()
