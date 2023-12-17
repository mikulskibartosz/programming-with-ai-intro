class Service:
    def __init__(self):
        self.users = {}

    def create(self, name, email):
        self.users[name] = email

    def get_all_users(self):
        return list(self.users.items())
    
    def get_user_by_name(self, name):
        for user_name, email in self.users.items():
            if user_name == name:
                return email
        return None
