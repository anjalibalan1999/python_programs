
# from rest_framework.decorators import detail_route
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template import loader

def index(request):
    # inject the respective values in HTML template
    html_message = loader.render_to_string(
        'message.html',
        {
            'name': 'Candidate',
            'body':  'I hope u doing well ',
        })    
    send_mail(
        'Congratulations!',
        'You are lucky to recieve this mail.',
        'yourEmail@gmail.com', # Update this with your mail id
        ['recipientEmail.com'],  # Update this with the recipients mail id
        html_message=html_message,
        fail_silently=False,
    )

    return HttpResponse("Email was successfully sended...!!")