from django.contrib.auth.models import User
import pytest

@pytest.fixture
def superAdmin() -> User:
    User.objects.create_user(
         'admin', 
         'omisolaidowu@gmail.com,',
       'cmosbattery',
       is_superuser=True
       )

