from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Match

# Create your views here.
def matches(request):
    mymatches = Match.objects.all().values()
    template = loader.get_template('myfirst.html')
    context = {
        'mymatches': mymatches,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template('create.html')
    return HttpResponse(template.render())