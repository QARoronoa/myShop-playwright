import time

from pagesObject.HomePage import HomePage
from pagesObject.ContactUsPage import ContactUsPage


def test_contact_us(setup):
    home_page = HomePage(setup)
    contactUs_page = ContactUsPage(setup)

    #click on contact us button
    home_page.verify_home_page_title()
    home_page.click_on_contact_us_link()
    contactUs_page.verify_redirected_to_contactUs_page()


    #remplir formulaire
    contactUs_page.fill_form_contact_us()
    contactUs_page.click_on_send_button()

    #verify message is sent
    contactUs_page.verify_success_message_is_visible()




