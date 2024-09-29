from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Don't give up, You hve just started")
    return render(request, 'website/test.html')

def about(request):
    return HttpResponse("You are talking to Era Chnager")

def contact(request):
    return HttpResponse("No need to contact me, just conatact God, everything will be solved")