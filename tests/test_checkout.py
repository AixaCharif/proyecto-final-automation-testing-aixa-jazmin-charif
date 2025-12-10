from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import json

# Cargar usuario
with open("data/user.json") as f:
    user = json.load(f)["user"]

def test_checkout_complete(driver):
    """Flujo completo: login → agregar producto → carrito → checkout → finalizar."""

    login_page = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    # Login
    login_page.login(user["username"], user["password"])

    # Agregar producto
    product_name = inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    # Validar que el producto esté en el carrito
    assert cart.get_cart_product_name() == product_name

    # Checkout
    cart.click_checkout()
    cart.fill_checkout_form("Aixa", "Charif", "1876")
    cart.finish_checkout()

    success_message = cart.get_success_message().strip().lower()

    assert "thank you for your order" in success_message, \
        f"Mensaje recibido: {success_message}"
