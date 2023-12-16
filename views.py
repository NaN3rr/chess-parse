#This is an general model for a Django implementation
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from site.models import Game #database

def game(request):
    template = loader.get_template("game.html")
    game = Game.objects.all().values()
    data = game[0] #index of requested game
    data = data["location"]
        
    context = {
        'data':data, #in template inData = '{{ data|escapejs }}';
    }
    return HttpResponse(template.render(context, request))
