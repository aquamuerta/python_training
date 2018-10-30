from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test1"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(name="Alexander"))
    app.contact.return_to_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)