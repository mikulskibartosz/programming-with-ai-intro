class Service:
    def __init__(self):
        self.users = {}

    def create(self, name, email):
        self.users[name] = email

    def get_all_users(self):
        return list(self.users.items())
