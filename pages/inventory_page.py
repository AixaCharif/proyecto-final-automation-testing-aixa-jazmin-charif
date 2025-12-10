# pages/inventory_page.py
from selenium.webdriver.common.by import By

class InventoryPage:

    TITLE = (By.CLASS_NAME, "title")
    PRODUCT_LIST = (By.CLASS_NAME, "inventory_item")
    FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_COUNTER = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(*self.TITLE).text

    def get_products(self):
        return self.driver.find_elements(*self.PRODUCT_LIST)

    def add_first_product_to_cart(self):
        products = self.get_products()
        first = products[0]
        button = first.find_element(By.TAG_NAME, "button")
        product_name = first.find_element(By.CLASS_NAME, "inventory_item_name").text
        button.click()
        return product_name

    def get_cart_count(self):
        return self.driver.find_element(*self.CART_COUNTER).text

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()
