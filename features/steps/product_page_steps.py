from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
CLOSING_X_SIDE_SECTION = (By.ID, 'attach-close_sideSheet-link')

COLOR_OPTIONS = (By.CSS_SELECTOR, 'div#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, 'div#variation_color_name span.selection')

@when('Click Add to card button')
def click_add_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()


@when('Close suggestions side section')
def close_side_suggestions(context):
    closing_btn = context.driver.find_elements(*CLOSING_X_SIDE_SECTION)
    if len(closing_btn) == 1:
        closing_btn[0].click()


@given('Open Amazon Dress {productid} page')
def open_dress_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}/')


@then('Verify user can select through colors')
def verify_colors(context):
    expected_colors = ['Black', 'Emerald', 'Ivory', 'Navy']
    color_webelements =  context.driver.find_elements(*COLOR_OPTIONS)
    # for x in range(len(color_webelements)):
    #     color_webelements[x].click()
    #     actual_color = context.driver.find_element(*SELECTED_COLOR).text
    #
    #     print(actual_color)
    #     assert actual_color == expected_colors[x], f'Expected {expected_colors[x]}, but got {actual_color}'

    for color in color_webelements:
        sleep(1)
        color.click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text

        assert actual_color == expected_colors[color_webelements.index(color)]
