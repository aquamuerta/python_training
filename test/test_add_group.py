# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
        old_groups = app.group.get_group_list()
        app.group.open_groups_page()
        group = Group(name="gdfhjtyr", header="werthnm", footer="etthjyure")
        app.group.create(group)
        app.group.return_to_groups_page()
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
