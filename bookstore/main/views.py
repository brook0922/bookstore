from django.shortcuts import render
from django.http import HttpResponse
import datetime

def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    now = datetime.datetime.now()
    Hello = []
    
    if 5 < now.hour < 12:
        Hello.append('歡迎光臨，來杯提神的咖啡吧')
    elif 17 > now.hour >= 12:
        Hello.append('歡迎光臨，來份下午茶吧')
    return HttpResponse(Hello)