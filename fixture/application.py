from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def open_home_page(self):
        wd = self.wd
        # open home page,
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def create_contact(self, contact):
         wd = self.wd
         #add new contact
         wd.find_element_by_link_text("add new").click()
         # fill contact form
         wd.find_element_by_name("firstname").click()
         wd.find_element_by_name("firstname").clear()
         wd.find_element_by_name("firstname").send_keys(contact.name)
         wd.find_element_by_name("lastname").click()
         wd.find_element_by_name("lastname").clear()
         wd.find_element_by_name("lastname").send_keys(contact.lastname)
         wd.find_element_by_name("address").click()
         wd.find_element_by_name("address").clear()
         wd.find_element_by_name("address").send_keys(contact.address)
         wd.find_element_by_name("email").click()
         wd.find_element_by_name("email").clear()
         wd.find_element_by_name("email").send_keys(contact.email)
         # submit contact creation
         wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()