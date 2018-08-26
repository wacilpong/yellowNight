from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from yellowBot.models import realtimedata
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
    today = datetime.date.today().strftime("%m월 %d일")
    
    return JsonResponse({
            'message': {
                'text': "오늘(" + today + ") 당신이 잠든 사이 N포털에서 가장 많이 검색한 키워드들을 확인해보세요!\n" + realtimedata.select()
            },
            'keyboard': {
                  'type': 'buttons',
                  'buttons' : ['AM 7:00', 'AM 8:00', 'AM 9:00']
            }
        })