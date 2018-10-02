

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
            wd = self.app.wd
            # add new contact
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

    def delete_first_contact(self):
            wd = self.app.wd
            # select first contact
            wd.find_element_by_name("selected[]").click()
            # submit deletion
            wd.find_element_by_xpath("//input[@value='Delete']").click()
            wd.switch_to_alert().accept()
