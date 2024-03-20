
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from korp.forms import *


def sendform(request):
    # --- sendform ------
    if request.method == 'POST':
        print("POST-------------------------------------------------")
        print(request.POST)
        client = request.POST['client']
        phone = request.POST['phone']
        categ = request.POST['categ']
        idprop = request.POST['idprop']
        titleprop = request.POST['titleprop']
        adresprop = request.POST['adresprop']

        print(request.POST)

        if client:
            subject = "Заявка на просмотр с gebo-commers.ru"
            body = {
                'Клиент': 'Клиент: ' + client,
                'Телефон': 'Телефон: ' + phone,
                'id': 'id объекта: ' + idprop,
                'Категория': 'Категория: ' + categ,
                'Заголовок': 'Заголовок: ' + titleprop,
                'Адрес': 'Адрес: ' + adresprop,

            }
            message = "\n".join(body.values())
            try:
                from django.conf import settings
                send_mail(subject, message,
                          settings.EMAIL_HOST,
                          ['ellips-web@yandex.ru'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
        else:
            raise Exception

        return None

    # --- sendform ------