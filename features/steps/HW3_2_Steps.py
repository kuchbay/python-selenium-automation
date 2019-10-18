from behave import when, then
from selenium.webdriver.common.by import By

@when('Click Help link')
def click_help_link(context):
    context.driver.find_element(By.XPATH, "//a[@class='nav_a' and @href='/gp/help/customer/display.html?ie=UTF8&nodeId=508510&ref_=footer_gw_m_b_he']").click()

@when('Type in Cancel Order')
def type_cancel_order(context):
    search = context.driver.find_element(By.XPATH, "//input[@id='helpsearch']")
    search.clear()
    search.send_keys('cancel order')
    context.driver.find_element(By.CLASS_NAME, 'a-button-input').click()

@then('Verify cancel order is displayed')
def verify_cancel_order_displayed(context):
    assert 'Cancel Items or Orders' in context.driver.find_element(By.XPATH, "//div[@class='help-content']").text

