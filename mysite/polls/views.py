from django.shortcuts import render


def index(request):
    return render(request, 'music/index.html', {'all_albums': all_albums})
