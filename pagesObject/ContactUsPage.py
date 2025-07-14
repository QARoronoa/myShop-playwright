from pagesObject.BasePage import BasePage


class ContactUsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)


    #locators
        self.customer_service_list = page.locator('#id_contact')
        self.email_address_field = page.locator('#email')
        self.order_reference_field = page.locator('#id_order')
        self.message_field = page.locator('#message')
        self.send_button = page.get_by_role('button', name='Send')
        self.alert_message = page.locator('.alert')

    #methodes

    def verify_redirected_to_contactUs_page(self):
        self.verify_title_of_page("Contact us - My Shop")

    def fill_form_contact_us(self):
        self.customer_service_list.select_option(value="1")
        self.fill_input_field(self.email_address_field, 'isdfs@slj.com')
        self.fill_input_field(self.order_reference_field, 'fjgh123')
        self.fill_input_field(self.message_field, 'test')


    def click_on_send_button(self):
        self.click_on_visible_element(self.send_button)

    def verify_success_message_is_visible(self):
        self.verify_contain_text(self.alert_message, 'successfully')


