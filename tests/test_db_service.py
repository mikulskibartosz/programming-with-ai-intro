import pytest
from rest.db_service import DbService

@pytest.fixture
def db_service():
    service = DbService()
    service.clear_table()
    yield service
    service.close()

def test_create_user(db_service):
    name = "John Doe"
    email = "john.doe@example.com"
    db_service.create(name, email)

    assert (name, email) in db_service.get_all_users()


def test_create_user_already_exists(db_service):
    name = "John Doe"
    email = "john.doe@example.com"
    db_service.create(name, email)

    with pytest.raises(Exception):
        db_service.create(name, email)


def test_get_all_users(db_service):
    name1 = "John Doe"
    email1 = "john.doe@example.com"
    db_service.create(name1, email1)

    name2 = "Jane Smith"
    email2 = "jane.smith@example.com"
    db_service.create(name2, email2)

    all_users = db_service.get_all_users()

    assert len(all_users) == 2
    assert (name1, email1) in all_users
    assert (name2, email2) in all_users

def test_get_user_by_name(db_service):
    name1 = "John Doe"
    email1 = "john.doe@example.com"
    db_service.create(name1, email1)

    user_exists = db_service.get_user_by_name(name1)
    assert user_exists == email1


def test_get_user_by_name_user_does_not_exist(db_service):
    name1 = "John Doe"
    email1 = "john.doe@example.com"
    db_service.create(name1, email1)

    user_does_not_exist = db_service.get_user_by_name("Jane Smith")
    assert user_does_not_exist is None


def test_update_user_email(db_service):
    name = "John Doe"
    email = "john.doe@example.com"
    db_service.create(name, email)

    new_email = "john.doe.new@example.com"
    db_service.update_email(name, new_email)

    all_users = db_service.get_all_users()
    assert (name, new_email) in all_users

def test_update_user_email_user_does_not_exist(db_service):
    name = "John Doe"
    email = "john.doe@example.com"
    db_service.create(name, email)

    new_name = "Jane Smith"
    new_email = "jane.smith@example.com"
    with pytest.raises(Exception):
        db_service.update_email(new_name, new_email)


def test_delete_user_by_name(db_service):
    name = "John Doe"
    email = "john.doe@example.com"
    db_service.create(name, email)

    db_service.delete_user_by_name(name)

    all_users = db_service.get_all_users()
    assert len(all_users) == 0


def test_create_user_rejects_invalid_email(db_service):
    name = "John Doe"
    invalid_email = "john.doe@example"
    with pytest.raises(Exception):
        db_service.create(name, invalid_email)


def test_update_user_rejects_invalid_email(db_service):
    name = "John Doe"
    email = "john.doe@example.com"
    db_service.create(name, email)

    invalid_email = "john.doe@example"
    with pytest.raises(Exception):
        db_service.update_email(name, invalid_email)
