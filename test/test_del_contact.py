from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test2"))
    old_contacts = app.contact.get_contact_list()
    app.open_home_page()
    app.contact.delete_first_contact()
    app.contact.return_to_home()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)