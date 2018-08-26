from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime

# Create your views here.

def keyboard(request):
    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['AM 7:00', 'AM 8:00', 'AM 9:00']
    })

@csrf_exempt
def message(request):
    data = ((request.body).decode('utf-8'))
    received_data = json.loads(data)
    # clicked_button = received_data['content']
    today = datetime.date.today().strftime("%m. %d")
    
    return JsonResponse({
            'message': {
                'text': "Today(" + today + ")'s midnight hot 10 topics !"
            },
            'keyboard': {
                  'type': 'buttons',
                  'buttons' : ['AM 7:00', 'AM 8:00', 'AM 9:00']
            }
        })