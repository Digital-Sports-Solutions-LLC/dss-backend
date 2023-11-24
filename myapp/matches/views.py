from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Match, MatchForm

def matches(request):
    mymatches = Match.objects.all().values()
    context = {
        'mymatches': mymatches,
    }
    template = loader.get_template('matches.html')
    return HttpResponse(template.render(context, request))

def create(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matches')  # Redirect to the 'matches' view after successful form submission
        else:
            print(form.errors)
    else:
        form = MatchForm()

    context = {
        'form': form,
    }
    
    template = loader.get_template('create.html')
    return HttpResponse(template.render(context, request))