from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class UrbanRoutesPage:
    # Seção De e Para
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    #Fluxo de chamada de taxi
    taxi_option = (By.XPATH, '//button[contains(text(),"Chamar")]')
    comfort_icon= (By.XPATH, '//img[contains(@src,"kids")]')
    comfort_active = (By.XPATH, '//div[contains(@class,"tcard") and contains(@class,"active") and .//img[contains(@src,"kids")]]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def _find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _type(self, locator, text):
        element = self._find(locator)
        element.clear()
        element.send_keys(text)

    def _get_text(self, locator):
        return self._find(locator).text

    def _get_value(self, locator):
        return self._find(locator).get_attribute('value')

    def enter_locations(self, from_text, to_text):
        self._type(self.from_field, from_text)
        self._type(self.to_field, to_text)

    def get_from_locations(self):
        return self._get_value(self.from_field)

    def get_to_locations(self):
        return self._get_value(self.to_field)

#Chamar táxi

    def click_taxi_option(self):
        self.driver.find_element(*self.taxi_option).click()

    def click_icon_comfort_selected(self):
        self.driver.find_element(*self.comfort_icon).click()

    def click_comfort_button(self):
        try:
            active_button = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.comfort_active)
            )
            return "active" in active_button.get_attribute("class")
        except Exception:
            return False