# README
Designing my own portfolio website in Django from scratch. Main aim is to learn Django and basics of web development using Django along the way.

## The Structure of a Django Website
A Django website consists of a single project that is split into separate apps. The idea is that each app handles a self-contained function that the site needs to perform. As an example, imagine an application like Instagram. There are several different functions that need to be performed:

* User management: Login, logout, register, and so on
* The image feed: Uploading, editing, and displaying images
* Private messaging: Private messages between users and notifications

These are each separate pieces of functionality, so if this were a Django site, then each piece of functionality should be a different Django app inside a single Django project.

The Django project holds some configurations that apply to the project as a whole, such as project settings, URLs, shared templates and static files. Each application can have its own database and has its own functions to control how the data is displayed to the user in HTML templates.

Each application also has its own URLs as well as its own HTML templates and static files, such as JavaScript and CSS.

Django apps are structured so that there is a separation of logic. It supports the Model-View-Controller Pattern, which is the architecture on which most web frameworks are built. The basic principle is that in each application there are three separate files that handle the three main pieces of logic separately:

* **Model** defines the data structure. This is usually a database and is the base layer to an application.
* **View** displays some or all of the data to the user with HTML and CSS.
* **Controller** handles how the database and the view interact.

### Folder structure of a Django Project:

* **__init__.py** tells Python to treat the directory as a Python package.
* **admin.py** contains settings for the Django admin pages.
* **apps.py** contains settings for the application configuration.
* **models.py** contains a series of classes that Django’s ORM converts to database tables.
* **tests.py** contains test classes
* **views.py** contains functions and classes that handle what data is displayed in the HTML templates.


### Creating a View

Views in Django are a collection of functions or classes inside the `views.py` file in your app directory. Each function or class handles the logic that gets processed each time a different URL is visited.

### Styling

If you don’t add any styling, then the app you create isn’t going to look too nice. Instead of going into CSS styling with this tutorial, we’ll just cover how to add bootstrap styles to your project. This will allow us to improve the look of the site without too much effort.

Before we get started with the Bootstrap styles, we’ll create a base template that we can import to each subsequent view. This template is where we’ll subsequently add the Bootstrap style imports.

We have created a `templates` folder in the `main_proj` directory, which will contain the html templates that will be used in all apps in the project. 

Each Django project can consist of multiple apps that handle separated logic, and each app contains its own templates directory to store HTML templates related to the application. 

This application structure works well for the backend logic, but we want our entire site to look consistent on the front end. Instead of having to import Bootstrap styles into every app, we can create a template or set of templates that are shared by all the apps. As long as Django knows to look for templates in this new, shared directory it can save a lot of repeated styles.