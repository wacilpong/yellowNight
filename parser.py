## parser.py
import requests
from bs4 import BeautifulSoup
import json
import os
## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yellowNight.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

## BlogData를 import해옵니다
from yellowBot.models import realtimedata

def parse_realtimekeyword():
    req = requests.get('https://www.naver.com/')
    html = req.text
    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        '.PM_CL_realtimeKeyword_rolling span[class*=ah_k]'
    )

    data = {}

    ## my_titles는 list 객체
    for title in my_titles:
    ## Tag안의 텍스트
        print(title.text)
        ## Tag의 속성을 가져오기(ex: class)
        #print(title.get('class'))

        data[title.text] = title.text

    return data

## 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
if __name__=='__main__':
    realtimekeyword = parse_realtimekeyword()
    for t, l in realtimekeyword.items():
        realtimedata(title=t, link=l).save()
   