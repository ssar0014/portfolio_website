from django.shortcuts import render

# defined a view function called hello world
# when function is called, it will render the hello_world.html template
# takes an argument - request - This object is an HttpRequestObject that is created whenever a page is loaded
# It contains information about the request, such as the method, which can take several values including GET and POST.
def hello_world(req):
    return render(req, "hello_world.html", {})
