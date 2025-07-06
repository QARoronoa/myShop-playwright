import time

from playwright.sync_api import Page
from pagesObject.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


    #locators
        self.email_register_field = page.locator('#email_create')
        self.create_account_button = page.locator('#SubmitCreate')
        self.title_mrs = page.locator('#id_gender1')
        self.firstName_field = page.locator('#customer_firstname')
        self.lastName_field = page.locator('#customer_lastname')
        self.password_field = page.locator('#passwd')
        self.dayBirth_field = page.locator('#days')
        self.monthBirth_field = page.locator('#months')
        self.yearBirth_field = page.locator('#years')
        self.register_button = page.get_by_role('button', name="Register" )
        self.email_login = page.locator('#email')
        self.password_login = page.locator('#passwd')
        self.signIn_button = page.get_by_role("button", name="Sign in")




    #methodes
    def enter_email_create_account(self, email):
        self.fill_input_field(self.email_register_field, email)

    def click_on_button_create_account(self):
        self.click_on_visible_element(self.create_account_button)

    def fill_form_create_account(self, firstName, lastName, password, dayBirth, monthBirth, yearBirth):
        self.title_mrs.click()
        self.fill_input_field(self.firstName_field, firstName)
        self.fill_input_field(self.lastName_field, lastName)
        self.fill_input_field(self.password_field, password)
        time.sleep(1)
        self.dayBirth_field.select_option(value=dayBirth)
        self.monthBirth_field.select_option(value=monthBirth)
        self.yearBirth_field.select_option(value=yearBirth)

    def click_on_register_button(self):
        self.click_on_visible_element(self.register_button)

    def enter_email_and_password(self, email, password):
        self.fill_input_field(self.email_login,email)
        self.fill_input_field(self.password_login, password)

    def click_on_signIn_button(self):
        self.click_on_visible_element(self.signIn_button)



