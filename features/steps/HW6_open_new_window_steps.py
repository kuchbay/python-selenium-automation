from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

DEALS_UNDER_25_LINK = (By.XPATH, "//a[contains(@aria-label, 'deals under $25')]")
TODAYS_DEALS_HEADER = (By.CSS_SELECTOR, 'h1.a-size-large')
PRODUCT_TO_ADD_TO_CART_SECTION = (By.XPATH, "//a[contains(@aria-label, 'Tommy')]")
FIRST_PRODUCT_TO_ADD_TO_CART = (By.CSS_SELECTOR, "img.oct-acs-asin-image.oct-dlp-asin-image")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add-to-cart-button")
CARD_ITEM_COUNT = (By.ID, 'nav-cart-count')

@when('Store original windows')
def store_current_windows(context):
    original_window = context.driver.current_window_handle
    old_windows = context.driver.window_handles


@when('Click to open Deals under 25')
def click_to_open_deals_under_25(context):
    context.driver.find_element(*DEALS_UNDER_25_LINK).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    new_window = current_windows[1]
    context.driver.switch_to_window(new_window)

@when('Click to add a product from deals to cart')
def add_product_from_deals_to_cart(context):
    context.driver.find_element(*PRODUCT_TO_ADD_TO_CART_SECTION).click()
    context.driver.find_element(*FIRST_PRODUCT_TO_ADD_TO_CART).click()
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()


@when('And User can close new window and switch back to original')
def close_current_window_and_switch_to_original(context):
    current_windows = context.driver.window_handles
    original_window = current_windows[0]
    context.driver.close()
    context.driver.switch_to_window(original_window)


@when('Refresh the page')
def refresh_page(context):
    context.driver.refresh()
    sleep(1)

@then("{expected_header} is shown")
def header_is_correct(context, expected_header):
    actual_header = context.driver.find_element(*TODAYS_DEALS_HEADER).text
    assert actual_header == expected_header, f'Expected {expected_header}, but got {actual_header}'


@then("Verify cart has {expected_item_count} item")
def verify_item_count(context, expected_item_count):
    actual_items = context.driver.find_element(*CARD_ITEM_COUNT).text
    assert actual_items == expected_item_count, f'Expected {expected_item_count}, but got {actual_items}'