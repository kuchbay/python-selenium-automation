from behave import when, then
from selenium.webdriver.common.by import By

@then('Shopping cart is empty')
def is_shopping_cart_empty(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "span#nav-cart-count").text == "0"


