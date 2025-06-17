from playwright.sync_api import Page

from pagesObject.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    #locators
        self.item_search = page.locator('.lighter')
        self.item_image = page.locator("div[itemtype='http://schema.org/Product']")
        self.more_button = page.get_by_role('link', name="More")

    #methodes
    def verify_redirected_to_search_page(self, title):
        self.verify_title_of_page(title)

    def verify_search_item_is_visible(self, text):
        self.verify_element_is_visible(self.item_search)
        self.verify_contain_text(self.item_search, text)

    def scroll_to_item_image(self):
        self.item_image.hover()

    def click_on_quick_view_button(self):
        self.click_on_visible_element(self.more_button)
