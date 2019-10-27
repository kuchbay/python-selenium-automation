from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, 'div#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, 'div#variation_color_name span.selection')
REGULAR_PRICES = (By.CSS_SELECTOR, 'li span.wfm-sales-item-card__regular-price')


@given('Open Amazon product {productid} page')
def open_dress_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}/')


@given('Open Amazon wholefoods {deals} page')
def open_wholefoodsdeals_page(context, deals):
    context.driver.get(f'https://www.amazon.com/{deals}/')


@then('Verify user can select through jean colors')
def verify_colors(context):
    expected_colors = ['Medium Wash', 'Dark Wash', 'Rinse']
    color_webelements =  context.driver.find_elements(*COLOR_OPTIONS)

    for color in color_webelements:
        sleep(1)
        color.click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text

        assert actual_color == expected_colors[color_webelements.index(color)]


@then('Verify every item has a word Regular')
def verify_regularprice_is_present(context):
    expected_word = 'Regular'
    products = context.driver.find_elements(*REGULAR_PRICES)
    for product in products:
        assert product.text.find(expected_word) != -1
