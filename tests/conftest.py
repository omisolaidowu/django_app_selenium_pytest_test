from django.contrib.auth.models import User
import pytest
import os
from dotenv import load_dotenv
load_dotenv('.env')
from django.test import LiveServerTestCase


@pytest.fixture(scope="class")
def superAdmin() -> User:
    return User.objects.create_user(
         'funmilayo',  
         'idowuomisola@gmail.com,',
       os.getenv('SUPER_ADMIN_PASSWORD'),
       is_superuser=True
       )


@pytest.mark.usefixtures("superAdmin")
class admin(LiveServerTestCase):
  @pytest.fixture(autouse=True)
  def super(self, superAdmin):
    self.createSuperAdmin = superAdmin
    return self.createSuperAdmin