from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'request':request
    }
    return render(request,'demo/index.html',context)