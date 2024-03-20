
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from korp.forms import *


def sendform(request):
    # --- sendform ------
    if request.method == 'POST':
        print("POST-------------------------------------------------")
        form = ContactForm(request.POST)

        print("form.is_valid()", form.is_valid())

        if form.is_valid():
            subject = "Заявка на просмотр с gebo-commers.ru"
            print("-------------------------------------------------")
            print("Заявка на просмотр с gebo-commers.ru")
            print(subject, form.cleaned_data['client'], form.cleaned_data['phone'], )
            body = {
                'Клиент': 'Клиент ' + form.cleaned_data['client'],
                'Телефон': 'Телефон ' + form.cleaned_data['phone'],

            }
            message = "\n".join(body.values())
            try:

                # import imaplib
                # import ssl
                # ctx = ssl.create_default_context()
                # ctx.set_ciphers('DEFAULT')
                # imapSrc = imaplib.IMAP4_SSL('mail.safemail.it', ssl_context=ctx)

                from django.conf import settings
                send_mail(subject, message,
                          settings.EMAIL_HOST,
                          ['ellips-web@yandex.ru'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            # return redirect("formsent/")
        else:
            raise Exception

        form = ContactForm()
        return form

    # --- sendform ------