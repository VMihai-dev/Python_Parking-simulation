from django.shortcuts import render
from . import server, entrance_client1, entrance_client2, exit_client2, exit_client1
# from django.http import HttpResponse, HttpResponseRedirect
from . import variables as myvars


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
    context = {
        'parkingSpaces': myvars.parkingSpaces,
        'queueSize': myvars.queue
    }
    if request.method == 'POST' and 'entrance1_script' in request.POST:
        entrance_client1.run_from_park()
        wait_for_change(context)
        return render(request, 'park/park.html', context)
    elif request.method == 'POST' and 'entrance2_script' in request.POST:
        entrance_client2.run_from_park()
        wait_for_change(context)
        return render(request, 'park/park.html', context)
    elif request.method == 'POST' and 'exit1_script' in request.POST:
        exit_client1.run_from_park()
        wait_for_change(context)
        return render(request, 'park/park.html', context)
    elif request.method == 'POST' and 'exit2_script' in request.POST:
        exit_client2.run_from_park()
        wait_for_change(context)
        return render(request, 'park/park.html', context)
    else:
        return render(request, 'park/park.html', context)


def wait_for_change(context):
    oldSpaces = context.get('parkingSpaces')
    oldQueue = context.get('queueSize')
    while oldSpaces == context.get('parkingSpaces') and oldQueue == context.get('queueSize'):
        context['parkingSpaces'] = myvars.parkingSpaces
        context['queueSize'] = myvars.queue