import json
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Cargar usuario
with open("data/user.json") as f:
    user = json.load(f)["user"]

def test_login_valid(driver):
    login_page = LoginPage(driver)
    inventory = InventoryPage(driver)

    login_page.login(user["username"], user["password"])

    assert inventory.get_title() == "Products", "El login no redirigió al inventario"
