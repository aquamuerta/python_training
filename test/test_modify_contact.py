from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test1"))
    app.contact.modify_first_contact(Contact(name="Alexander"))
    app.contact.return_to_home_page()
