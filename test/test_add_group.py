# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
        app.open_home_page()
        app.session.login("admin", "secret")
        app.group.open_groups_page()
        app.group.create(Group(name="gdfhjtyr", header="werthnm", footer="etthjyure"))
        app.session.logout()

