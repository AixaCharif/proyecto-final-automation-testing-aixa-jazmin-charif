# pages/cart_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    CART_ITEM = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    CHECKOUT_BUTTON = (By.ID, "checkout")

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_product_name(self):
        item = self.driver.find_element(*self.CART_ITEM)
        return item.find_element(*self.PRODUCT_NAME).text

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def fill_checkout_form(self, name, last_name, postal):
        self.driver.find_element(*self.FIRST_NAME).send_keys(name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def finish_checkout(self):
        finish_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "finish"))
        )
        finish_btn.click()

        # Validar página final
        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-text"))
        )


    def get_success_message(self):
        return self.driver.find_element(*self.COMPLETE_HEADER).text
