import pytest
from playwright.sync_api import Playwright

from data.LoginData import Login
from data.AccountData import Account
@pytest.fixture(scope="function")
def setup(playwright: Playwright, request):
     browser = playwright.webkit.launch(headless=False)
     # context = browser.new_context(record_video_dir="videos/")
     context = browser.new_context()
     context.tracing.start(screenshots=True, snapshots=True, sources=True)

     page = context.new_page()
     # page.set_viewport_size({'width':1920, 'height': 1080})
     page.goto("http://www.automationpractice.pl/index.php")
     yield page

     context.tracing.stop(path="trace.zip")
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
def wrong_password():
     return {"emailAdress" : "roronoa12@ymail.com", "password": "1234567890"}

@pytest.fixture()
def create_account():
     return {"emailAdress" : "roronoa12@ymail.com"}

@pytest.fixture
def address_form():
     return Account.fill_address_form()