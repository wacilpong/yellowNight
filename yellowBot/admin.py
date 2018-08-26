from django.contrib import admin
from .models import realtimedata

# Register your models here.
## 아래의 코드를 입력하면 realtimedata를 admin 페이지에서 관리할 수 있습니다.
admin.site.register(realtimedata)