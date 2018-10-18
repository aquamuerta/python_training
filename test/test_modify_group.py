from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.open_groups_page()
    group = Group(name="New group")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    app.contact.return_to_home()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
    #if app.group.count() == 0:
        #app.group.create(Group(header="test"))
    #old_groups = app.group.get_group_list()
    #app.group.open_groups_page()
    #app.group.modify_first_group(Group(header="New header"))
    #app.contact.return_to_home()
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)