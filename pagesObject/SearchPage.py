from playwright.sync_api import Page

from pagesObject.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    #locators
        self.item_search = page.locator('.lighter')

    #methodes
    def verify_redirected_to_search_page(self, title):
        self.verify_title_of_page(title)

    def verify_search_item_is_visible(self, text):
        self.verify_element_is_visible(self.item_search)
        self.verify_contain_text(self.item_search, text)
