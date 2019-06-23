from django.shortcuts import render
import datetime

def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    now = datetime.datetime.now()
    if 5 < now.hour < 12:
        msg = '早安！歡迎光臨，來杯提神的咖啡吧！'
    elif 17 > now.hour >= 12:
        msg = '午安！歡迎光臨，來份悠閒的下午茶吧！'
    else:
        msg = '晚安！歡迎光臨，今天也辛苦了！'
    context = {'msg':msg}
    return render(request, 'main/main.html', context)

def about (request):
    return render(request, 'about/about.html')