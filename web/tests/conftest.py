import pytest

from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from tests.users.factories import UserFactory


@pytest.fixture()
def auth_client(test_user):
    client = APIClient()
    # TODO: add an authorization code to the client
    # created vshagur@gmail.com, 2021-07-1
    return client


@pytest.fixture()
def anon_client():
    client = APIClient()
    return client


@pytest.fixture()
def test_user():
    User = get_user_model()
    return User.objects.all().last()


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        UserFactory()
        # TODO: add test database initialization here
        # created vshagur@gmail.com, 2021-07-1
        yield
