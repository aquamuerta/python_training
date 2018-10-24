# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
        old_contacts = app.contact.get_contact_list()
        app.contact.create(Contact("Anastasia", "Svettsova", "Spb", "test@test.com"))
        app.contact.return_to_home_page()
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)

