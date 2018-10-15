from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test2"))
    app.open_home_page()
    app.contact.delete_first_contact()
    app.contact.return_to_home()
