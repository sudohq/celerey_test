#coding=utf8
from django.http import HttpResponse
from main.tasks import *
from django.core.mail import send_mail

def ur(request):
    return HttpResponse('Какой-то раздел')

def pars(request, parse = None):
    url = 'http://%s%s' % (str(request.get_host()), str(request.get_full_path()))
    r_string = 'Вводимый URL:%s' % url
    parse_to_send.delay(url = parse)
    return HttpResponse(r_string)