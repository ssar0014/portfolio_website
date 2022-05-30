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