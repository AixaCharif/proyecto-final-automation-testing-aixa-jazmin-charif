import json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

# Cargar usuario
with open("data/user.json") as f:
    user = json.load(f)["user"]

def test_add_product_to_cart(driver):
    login_page = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login_page.login(user["username"], user["password"])

    product_name = inventory.add_first_product_to_cart()
    assert inventory.get_cart_count() == "1"

    inventory.go_to_cart()

    assert cart.get_cart_product_name() == product_name
