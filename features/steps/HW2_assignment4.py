from behave import given, when, then
from selenium.webdriver.common.by import By

@given('Open Amazon home page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click orders link')
def click_orders_link(context):
    context.driver.find_element(By.CSS_SELECTOR, "a#nav-orders span.nav-line-2").click()

@then('Verify Sign In page is opened')
def verify_signin_opened(context):
    #context.driver.find_element(By.CSS_SELECTOR, "input[type='email']")
    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url

