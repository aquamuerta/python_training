# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
        old_contacts = app.contact.get_contact_list()
        contact = Contact("Anastasia", "Svettsova", "Spb", "test@test.com")
        app.contact.create(contact)
        app.contact.return_to_home_page()
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        print(old_contacts)
        print(new_contacts)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

