from rest.service import Service

def test_create_user():
    service = Service()
    name = "John Doe"
    email = "john.doe@example.com"
    service.create(name, email)

    assert service.users[name] == email


def test_get_all_users():
    service = Service()
    name1 = "John Doe"
    email1 = "john.doe@example.com"
    service.create(name1, email1)

    name2 = "Jane Smith"
    email2 = "jane.smith@example.com"
    service.create(name2, email2)

    all_users = service.get_all_users()

    assert len(all_users) == 2
    assert (name1, email1) in all_users
    assert (name2, email2) in all_users

def test_get_user_by_name():
    service = Service()
    name1 = "John Doe"
    email1 = "john.doe@example.com"
    service.create(name1, email1)

    user_exists = service.get_user_by_name(name1)
    assert user_exists == email1


def test_get_user_by_name_user_does_not_exist():
    service = Service()
    name1 = "John Doe"
    email1 = "john.doe@example.com"
    service.create(name1, email1)

    user_does_not_exist = service.get_user_by_name("Jane Smith")
    assert user_does_not_exist is None


