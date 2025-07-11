from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import Members

def members(request: HttpRequest):
    template = loader.get_template('all_members.html')
    my_members = Members.objects.all()
    context = {
        'members': my_members,
    }
    return HttpResponse(template.render(context, request))

def details(request: HttpRequest, member_id: int):
    template = loader.get_template('details.html')
    member = Members.objects.get(id=member_id)
    context = {
        'member': member,
    }
    return HttpResponse(template.render(context, request))