# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
        fixture = Application()
        request.addfinalizer(fixture.destroy)
        return fixture

    
def test_add_contact(app):
        app.open_home_page()
        app.session.login("admin", "secret")
        app.contact.create(Contact("Anastasia", "Svettsova", "Spb", "test@test.com"))
        app.session.logout()

