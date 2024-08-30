from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the Demo Login Page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://www.saucedemo.com/")

@when('I fill the account information for account "{user}" into the Username field and the Password field')
def step_impl(context, user):
    context.driver.find_element(By.ID, "user-name").send_keys(user)
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")

@when('I click the Login Button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()

@then('I am redirected to the Demo Main Page')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "inventory_container")))

@then('I verify the App Logo exists')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "app_logo").is_displayed()

@then('I verify the Error Message contains the text "Sorry, this user has been banned."')
def step_impl(context):
    error_message = context.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert "Sorry, this user has been banned." in error_message.text

# Additional steps for the ordering scenario
@given('I am on the inventory page')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/inventory.html")

@when('user sorts products from high price to low price')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "product_sort_container").click()
    context.driver.find_element(By.XPATH, "//option[text()='Price (high to low)']").click()

@when('user adds the highest priced product')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//button[text()='Add to cart'])[1]").click()

@when('user clicks on cart')
def step_impl(context):
    context.driver.find_element(By.ID, "shopping_cart_container").click()

@when('user clicks on checkout')
def step_impl(context):
    context.driver.find_element(By.ID, "checkout").click()

@when('user enters first name "{first_name}"')
def step_impl(context, first_name):
    context.driver.find_element(By.ID, "first-name").send_keys(first_name)

@when('user enters last name "{last_name}"')
def step_impl(context, last_name):
    context.driver.find_element(By.ID, "last-name").send_keys(last_name)

@when('user enters zip code "{zip_code}"')
def step_impl(context, zip_code):
    context.driver.find_element(By.ID, "postal-code").send_keys(zip_code)

@when('user clicks Continue button')
def step_impl(context):
    context.driver.find_element(By.ID, "continue").click()

@then('I verify in Checkout overview page if the total amount for the added item is "$49.99"')
def step_impl(context):
    total_amount = context.driver.find_element(By.CLASS_NAME, "summary_total_label").text
    assert "$49.99" in total_amount

@when('user clicks Finish button')
def step_impl(context):
    context.driver.find_element(By.ID, "finish").click()

@then('Thank You header is shown in Checkout Complete page')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "complete-header").is_displayed()

def after_scenario(context, scenario):
    context.driver.quit()
