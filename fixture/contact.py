from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
            wd = self.app.wd
            # add new contact
            wd.find_element_by_link_text("add new").click()
            self.fill_contact_form(contact)
            # submit contact creation
            wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
            self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_home_page(self):
            wd = self.app.wd
            if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("address")) > 0):
                wd.find_element_by_link_text("home page").click()

    def return_to_home(self):
            wd = self.app.wd
            if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("address")) > 0):
                wd.find_element_by_link_text("home").click()

    def modify_first_contact (self, new_contact_data):
            wd = self.app.wd
            self.select_first_contact()
            # open modification form
            wd.find_element_by_xpath("//img[@alt='Edit']").click()
            # fill group form
            self.fill_contact_form(new_contact_data)
            # submit modification
            wd.find_element_by_name("update").click()
            self.contact_cache = None

    def delete_first_contact(self):
            wd = self.app.wd
            self.select_first_contact()
            # submit deletion
            wd.find_element_by_xpath("//input[@value='Delete']").click()
            wd.switch_to_alert().accept()
            self.contact_cache = None

    def select_first_contact(self):
            wd = self.app.wd
            # select first contact
            wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                text = element.find_elements_by_tag_name("td")
                lastname = text[1].text
                name = text[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=lastname, name=name, id=id))
        return list(self.contact_cache)




