from model.group import Group


def test_modify_group_name(app):
    app.group.open_groups_page()
    app.group.modify_first_group(Group(name="New group"))
    app.contact.return_to_home()


def test_modify_group_header(app):
    app.group.open_groups_page()
    app.group.modify_first_group(Group(header="New header"))
    app.contact.return_to_home()
