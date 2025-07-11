from django.http import HttpResponse, HttpRequest
from django.template import loader

def members(request: HttpRequest):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())