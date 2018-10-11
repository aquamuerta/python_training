# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
        app.open_home_page()
        app.session.login("admin", "secret")
        app.contact.create(Contact("Anastasia", "Svettsova", "Spb", "test@test.com"))
        app.contact.return_to_home_page()
        app.session.logout()

