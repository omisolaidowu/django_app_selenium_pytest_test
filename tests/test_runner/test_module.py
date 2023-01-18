import pytest
import sys
sys.path.append(sys.path[0] + "/..")
from setup.setup import Settings

from django.test import LiveServerTestCase


from sel_locators.sel_locators import Webactions


setup = Settings()


from django.contrib.auth.models import User


blog = Webactions(setup.driver)


@pytest.mark.usefixtures("superAdmin")
class TestUserLoginFormSuccess(LiveServerTestCase):

   @pytest.fixture(autouse=True)
   def super(self, superAdmin):
      self.createSuperAdmin = superAdmin
      return self.createSuperAdmin
      

   def test_should_post_blog(self):

      setup.setup()

      self.createSuperAdmin

      assert User.objects.count() == 1, "There should be only one superuser"

      blog.getWeb(self.live_server_url+'/login')
      assert "Log" in blog.getTitle(), "Error, log not in title"

      blog.fill_username('admin')
      blog.fill_password('cmosbattery')
      blog.submit_login()

      blog.getWeb(str(blog.current_url()))

      assert "Management" in blog.getTitle(), "Management must be on the next page"
      
      blog.published_yes()
      blog.enter_title("My First Blog")
      blog.write_content("Some lorem will be dumped here")
      blog.enter_description("Some blog descriptions")
      blog.submit_post()

      blog.getWeb(str(blog.current_url()))
      assert "Blog" in blog.getTitle(), "Blog must be on the next page"
      setup.tearDown()