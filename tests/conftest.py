from django.contrib.auth.models import User
import pytest
import os
from dotenv import load_dotenv
load_dotenv('.env')



@pytest.fixture
def superAdmin() -> User:
    User.objects.create_user(
         'admin', 
         'omisolaidowu@gmail.com,',
       os.getenv('SUPER_ADMIN_PASSWORD'),
       is_superuser=True
       )

