from setup.setup import Settings

from conftest import admin

from sel_locators.sel_locators import Webactions

from django.contrib.auth.models import User



setUp = Settings()


blog = Webactions(setUp.driver)

class TestUserLoginFormSuccess(admin):

   def test_should_post_blog(self):
      setUp.setup()

      self.createSuperAdmin

      assert User.objects.count() == 1, "There should be only one superuser"

      blog.getWeb(self.live_server_url+'/login')
      # blog.getWeb('https://django-app-selenium-pytest-test.vercel.app/login')
      assert "Log" in blog.getTitle(), "Error, log not in title"

      blog.fill_username('omisolaidowu') 
      blog.fill_password('idowupaul')
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
      setUp.tearDown()