from playwright.sync_api import Page, Locator, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def verify_title_of_page(self, title):
        expect(self.page).to_have_title(title)

    def verify_element_is_visible(self, element):
        expect(element).to_be_visible()

    def verify_contain_text(self, element, text):
        expect(element).to_contain_text(text)

    def click_on_visible_element(self, locator: Locator):
        expect(locator).to_be_visible()
        locator.click()

    def fill_input_field(self, locator: Locator, text):
        locator.wait_for(state="visible")
        locator.clear()
        locator.fill(text)