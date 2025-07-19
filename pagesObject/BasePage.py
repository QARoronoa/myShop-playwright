import allure
from playwright.sync_api import Page, Locator, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Vérifier le titre de la page : '{title}'")
    def verify_title_of_page(self, title):
        expect(self.page).to_have_title(title)

    @allure.step("Vérifier que l'élément est visible")
    def verify_element_is_visible(self, element):
        expect(element).to_be_visible()

    @allure.step("Vérifier que l'élément contient le texte : '{text}'")
    def verify_contain_text(self, element, text):
        expect(element).to_contain_text(text)

    @allure.step("Cliquer sur un élément visible")
    def click_on_visible_element(self, locator: Locator):
        expect(locator).to_be_visible()
        expect(locator).to_be_enabled()
        locator.click()

    @allure.step("Remplir le champ avec : '{text}'")
    def fill_input_field(self, locator: Locator, text):
        locator.wait_for(state="visible")
        locator.clear()
        locator.fill(text)