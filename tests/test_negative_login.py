import pytest

@pytest.mark.parametrize(
    "username,password,expected_message",
    [
        ("standard_user", "wrong_pass",
         "Epic sadface: Username and password do not match any user in this service"),

        ("wrong_user", "secret_sauce",
         "Epic sadface: Username and password do not match any user in this service"),

        ("", "secret_sauce",
         "Epic sadface: Username is required"),

        ("standard_user", "",
         "Epic sadface: Password is required"),
    ],
    ids=[
        "contrasena_incorrecta",
        "usuario_incorrecto",
        "usuario_vacio",
        "contrasena_vacia",
    ]
)
def test_login_invalid(driver, username, password, expected_message):
    from pages.login_page import LoginPage

    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(username, password)

    assert login_page.get_error_message() == expected_message
