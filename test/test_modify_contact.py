from model.contact import Contact


def test_modify_contact_name(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(name="Alexander"))
    app.session.logout()
