from django.shortcuts import render, HttpResponseRedirect
from main.models import Game, GameRequest
from main.forms import RequestGameForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RequestGameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            GameRequest.objects.create(username=form.cleaned_data['username'],
                                       email=form.cleaned_data['email'],
                                       gametitle=form.cleaned_data['gametitle'],
                                       officialsite=form.cleaned_data['officialsite']).save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks')
    else:
        # if a GET (or any other method) we'll create a blank form
        form = RequestGameForm()
    data = {'Games': [game.__dict__ for game in Game.objects.all()],
            'form': form}
    return render(request, 'main/index.html', data)


def gamepage(request, game):
    gameinfo = Game.objects.get(shortname=game).__dict__
    return render(request, 'main/gamepage.html', gameinfo)


def aboutus(request):
    return render(request, 'main/aboutus.html')


def thanks(request):
    return render(request, 'main/thanks.html')
