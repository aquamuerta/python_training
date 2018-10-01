from selenium import webdriver

class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.wd
        # fill group form
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()



    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

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