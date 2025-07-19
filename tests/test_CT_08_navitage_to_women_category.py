from pagesObject.HomePage import HomePage
from pagesObject.Category_Page import Category_Page


def test_vavigate_to_women_category(setup):
    home_page = HomePage(setup)
    category_page = Category_Page(setup)

    #verify home page
    home_page.verify_home_page_title()

    #click on women category
    home_page.click_on_women_category()
    category_page.verify_title_of_page("Women - My Shop")

