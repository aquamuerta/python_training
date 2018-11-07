class Contact:
    def __init__(self, name=None, lastname=None, address=None, email=None, id=None):
        self.name = name
        self.lastname = lastname
        self.address = address
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

