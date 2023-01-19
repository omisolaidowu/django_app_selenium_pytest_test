# Blog App
A demonstration of how to test Django app locally using Selenium and Pytest while connected to a remote cloud grid. The test for this blog app uses Selenium's LiveServerTestCase to access an instance of the cloud tunnel. It then combines the page object model (POM) with Pytest fixtures to create a superuser to access and test the blog publishing functionality. 

## To Run the Test

Activate your virtual environment and install dependencies:

```pip -r install requirements.txt```

Cd into blog-app/blog-app from the base directory:

```cd blog-app/blog-app```

Run the test by using the pytest command:

```pytest```

Pytest will look for the pytest.ini module and use that to point the test to the Django app settings. Pytest then automatically discovers declared test fixtures by looking inside the conftest.py file before running the test_module.py file. 

## Project Structure

```
Blog-App

├─ .gitignore
├─ manage.py
├─ no_idea
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ models.py
│  ├─ templates
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ null_project
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ pytest.ini
├─ requirements.txt
├─ tests
│  ├─ conftest.py
│  ├─ sel_locators
│  │  └─ sel_locators.py
│  ├─ setup
│  │  └─ setup.py
│  └─ test_runner
│     └─ test_module.py
└─ vercel.json
```

This project is live at https://django-app-selenium-pytest-test.vercel.app/