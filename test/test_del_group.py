
def test_delete_first_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.open_groups_page()
    app.group.delete_first_group()
    app.session.logout()