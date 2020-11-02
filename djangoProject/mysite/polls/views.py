from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import server, entrance_client1, exit_client2, exit_client1, entrance_client2
#from .... import server

availableParking = 5
context = {
    'spaces': availableParking
}

def home(request):
    if request.method == 'POST' and 'run_script' in request.POST:
        server.run_on_click()
        return render(request, 'polls/home.html')
    elif request.method == 'POST' and 'run_script2' in request.POST:
        entrance_client1.run_on_click()
        return render(request, 'polls/home.html')
    elif request.method == 'POST' and 'run_script3' in request.POST:
        entrance_client2.run_on_click()
        return render(request, 'polls/home.html')
    elif request.method == 'POST' and 'run_script4' in request.POST:
        exit_client1.run_on_click()
        return render(request, 'polls/home.html')
    elif request.method == 'POST' and 'run_script5' in request.POST:
        exit_client2.run_on_click()
        return render(request, 'polls/home.html')
    else:
        return render(request, 'polls/home.html')
# Create your views here.

def about(request):
    if request.method == 'POST' and 'run_script' in request.POST:
        entrance_client1.run_on_click2()
        return render(request, 'polls/about.html')
    elif request.method == 'POST' and 'run_script2' in request.POST:
        entrance_client2.run_on_click2()
        return render(request, 'polls/about.html')
    elif request.method == 'POST' and 'run_script3' in request.POST:
        exit_client1.run_on_click2()
        return render(request, 'polls/about.html')
    elif request.method == 'POST' and 'run_script4' in request.POST:
        exit_client2.run_on_click2()
        return render(request, 'polls/about.html')
    else:
        return render(request, 'polls/about.html')
# Create your views here.