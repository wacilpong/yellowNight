from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['AM 7:00', 'AM 8:00', 'AM 9:00']
    })
