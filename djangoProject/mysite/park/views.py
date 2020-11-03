from django.shortcuts import render
from . import server, entrance_client1, entrance_client2, exit_client2, exit_client1
# from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    if request.method == 'POST' and 'server_script' in request.POST:
        server.run_on_click()
        return render(request, 'park/home.html')
    elif request.method == 'POST' and 'entrance1_script' in request.POST:
        entrance_client1.run_from_home()
        return render(request, 'park/home.html')
    elif request.method == 'POST' and 'entrance2_script' in request.POST:
        entrance_client2.run_from_home()
        return render(request, 'park/home.html')
    elif request.method == 'POST' and 'exit1_script' in request.POST:
        exit_client1.run_from_home()
        return render(request, 'park/home.html')
    elif request.method == 'POST' and 'exit2_script' in request.POST:
        exit_client2.run_from_home()
        return render(request, 'park/home.html')
    else:
        return render(request, 'park/home.html')


def park(request):
    if request.method == 'POST' and 'entrance1_script' in request.POST:
        entrance_client1.run_from_park()
        return render(request, 'park/park.html')
    elif request.method == 'POST' and 'entrance2_script' in request.POST:
        entrance_client2.run_from_park()
        return render(request, 'park/park.html')
    elif request.method == 'POST' and 'exit1_script' in request.POST:
        exit_client1.run_from_park()
        return render(request, 'park/park.html')
    elif request.method == 'POST' and 'exit2_script' in request.POST:
        exit_client2.run_from_park()
        return render(request, 'park/park.html')
    else:
        return render(request, 'park/park.html')
