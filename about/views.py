from django.shortcuts import render
from about.models import Aboutmyself
import datetime

def home(request):
    return render(request, 'about/home.html')

def whoami(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    browser = request.META['HTTP_USER_AGENT']
    today = datetime.datetime.now()
    date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
    Aboutmyself.objects.create(browser=browser, ip=ip, datetimenow=today)
    
    return render(request, 'about/whoami.html', context={'browser':browser, 'ip':ip, 'date_time':date_time})
    