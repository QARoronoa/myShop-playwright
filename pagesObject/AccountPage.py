from playwright.sync_api import Page
from pagesObject.BasePage import BasePage


class AccountPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


        #locators
        self.alert_success_message = page.locator('p.alert')

        #methodes
    def verify_redirection_to_myAccount(self, title):
        self.verify_title_of_page(title)

    def verify_sucess_message_creation_account(self):
        self.verify_contain_text(self.alert_success_message, "Your account has been created.")





