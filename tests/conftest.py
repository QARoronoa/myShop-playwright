import pytest
from data.LoginData import Login
from data.AccountData import Account
@pytest.fixture(scope="function")
def setup(playwright, request):
     browser = playwright.chromium.launch(headless=False)
     context = browser.new_context()

     page = context.new_page()
     page.goto("http://www.automationpractice.pl/index.php")
     yield page

     context.close()
     browser.close()

@pytest.fixture(scope="function")
def enter_email_create_account():
     return Login.email_create_account()

@pytest.fixture(scope="function")
def fill_out_form():
     return Login.form_create_account()

@pytest.fixture
def login_valid():
     return {"emailAdress" : "roronoa12@ymail.com", "password": "123456"}

@pytest.fixture
def address_form():
     return Account.fill_address_form()