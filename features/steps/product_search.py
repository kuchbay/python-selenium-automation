from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]")
RESULTS = (By.XPATH, "//div[@class='g']")
NUMBER_OF_BOXES = (By.XPATH, "//div[contains(@class, 'a-section benefit-box benefit-box')]")

COLOR_OPTIONS = (By.CSS_SELECTOR, 'div#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, 'div#variation_color_name span.selection')


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')

@given('Open Amazon Prime page')
def open_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime/')



@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)


@then('First result contains {search_word}')
def verify_first_result(context, search_word):
    first_result = context.driver.find_element(*RESULTS).text
    print('\n{}'.format(first_result))
    assert search_word in first_result, "Expected word '{}' in message, but got '{}'".format(search_word, first_result)


#HW4 function to verify that Amazon prime page has 8 boxes
@then('Amazon Prime page has 8 boxes')
def verify_number_of_boxes(context):
    assert len(context.driver.find_elements(*NUMBER_OF_BOXES)) == 8, \
        f'Expected 8 items but got {len(context.driver.find_elements(*NUMBER_OF_BOXES))}'



