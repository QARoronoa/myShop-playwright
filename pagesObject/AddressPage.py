from playwright.sync_api import Page

from pagesObject.BasePage import BasePage


class AddressPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    #locators
        self.address_field = page.locator('#address1')
        self.city_field = page.locator('#city')
        self.state_field = page.locator('#id_state')
        self.zipCode_field = page.locator('#postcode')
        self.homePhone_field = page.locator('#phone')
        self.mobilePhone_field = page.locator('#phone_mobile')
        self.address_title_ref = page.locator('#alias')
        self.save_button = page.locator('#submitAddress')
        self.proceed_to_checkout = page.get_by_role('button', name='Proceed to checkout')

    #methodes
    def fill_address_form(self, address, city, zipCode, homePhone, mobilePhone, addressTitle):
        self.fill_input_field(self.address_field, address)
        self.fill_input_field(self.city_field, city)
        self.state_field.select_option(value="4")
        self.fill_input_field(self.zipCode_field, zipCode)
        self.fill_input_field(self.homePhone_field, homePhone)
        self.fill_input_field(self.mobilePhone_field, mobilePhone )
        self.fill_input_field(self.address_title_ref, addressTitle )
        self.click_on_visible_element(self.save_button)

    def click_on_proceed_to_checkout(self):
        self.click_on_visible_element(self.proceed_to_checkout)