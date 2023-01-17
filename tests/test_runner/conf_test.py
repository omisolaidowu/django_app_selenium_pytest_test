import pytest
from selenium import webdriver

from django.urls import reverse

# from tests.setup.setup import driver

# from tests.setup.setup import testSet
import sys
sys.path.append(sys.path[0] + "/..")
from setup.setup import testSet

from sel_locators.sel_locators import Webactions

from django.test import LiveServerTestCase


setup = testSet()

website = Webactions(setup.driver)




pytestmark = pytest.mark.django_db
from django.contrib.auth.models import User


from django.conf import settings

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




@pytest.mark.django_db
class TestUserLoginFormSuccess(LiveServerTestCase):
   def test_view(self):
      setup.testSetup()

      User.objects.create_user(
         'admin', 
         'omisolaidowu@gmail.co,',
       'cmosbattery', 
       is_superuser=True
       )
      assert User.objects.count() == 1, "There should be only one superuser"

      website.test_getWeb(self.live_server_url+'/login')
      assert "Log" in website.test_getTitle(), "Error, log not in title"

      website.fill_username('admin')
      website.fill_password('cmosbattery')
      website.submit_login()

      website.test_getWeb(str(website.current_url()))

      assert "Management" in website.test_getTitle(), "Management must be on the next page"
      
      website.published_yes()
      website.enter_title("My First Blog")
      website.write_content("Some lorem will be dumped here")
      website.enter_description("Some blog descriptions")
      website.submit_post()

      setup.driver.implicitly_wait(20)

      website.test_getWeb(str(website.current_url()))
      assert "Blog" in website.test_getTitle(), "Blog must be on the next page"
      setup.tearDown()