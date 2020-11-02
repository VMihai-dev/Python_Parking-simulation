from django.shortcuts import render
from django.http import HttpResponse
#from .... import server

availableParking = 5
context = {
    'spaces': availableParking
}
def home(request):
    return render(request, 'polls/home.html')
# Create your views here.

def about(request):
    return render(request, 'polls/about.html', context)
# Create your views here.