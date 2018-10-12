from model.contact import Contact


def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(name="Alexander"))
    app.contact.return_to_home_page()
