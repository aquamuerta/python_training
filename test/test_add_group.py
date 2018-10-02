# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
        fixture = Application()
        request.addfinalizer(fixture.destroy)
        return fixture


def test_add_group(app):
        app.open_home_page()
        app.session.login("admin", "secret")
        app.group.open_groups_page()
        app.group.create(Group(name="gdfhjtyr", header="werthnm", footer="etthjyure"))
        app.session.logout()

