from pagesObject.BasePage import BasePage

class Category_Page(BasePage):
    def __init__(self, page):
        super().__init__(page)


    #locators

    #methodes

    def verify_category_page_title(self):
        self.verify_title_of_page("Women - My Shop")