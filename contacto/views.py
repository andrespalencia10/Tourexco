import ssl, smtplib
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.conf import settings


def formulario_contacto(request):
    return render(request, 'contacto/contacto.html')


def contacto(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # phone =
        # email_message = union de todos los campos

        email_message = ''

        context = ssl._create_unverified_context()

        try:
            # TODO:
            # 1. El subject
            # 2. El cuerpo del mensaje tenga email, message y
            # 3. Agregar el campo telefono
            # 4. mostrar el mensaje y redirigir a la página de contacto

            with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
                server.ehlo()
                server.starttls(context=context)

                server.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)

                server.sendmail(
                    settings.EMAIL_USER,
                    settings.EMAIL_USER,
                    email_message
                )

                return HttpResponse('Gracias por contactarnos')

        except Exception as e:
            return HttpResponse(f'Ha ocurrido un error al enviar el mensaje: {str(e)}')

    return render(request, 'contacto/contacto.html')