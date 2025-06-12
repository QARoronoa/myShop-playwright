from pagesObject.BasePage import BasePage
from playwright.sync_api import Page, expect


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    #locators
        self.signIn_button = page.locator(".login")
        self.userAccount_link = page.locator('.account')

    #methodes
    def verify_home_page_title(self):
        self.verify_title_of_page("My Shop")

    def click_on_signIn_button(self):
        self.click_on_visible_element(self.signIn_button)

    def verify_user_is_connected(self):
        expect(self.userAccount_link).to_be_visible()

