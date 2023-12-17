class Service:
    def __init__(self):
        self.users = {}

    def create(self, name, email):
        if name in self.users:
            raise Exception("User already exists")
        self.users[name] = email

    def get_all_users(self):
        return list(self.users.items())
    
    def get_user_by_name(self, name):
        for user_name, email in self.users.items():
            if user_name == name:
                return email
        return None

    def update_email(self, name, new_email):
        if name in self.users:
            self.users[name] = new_email
        else:
            raise Exception("User does not exist")

    def delete_user_by_name(self, name):
        if name in self.users:
            del self.users[name]