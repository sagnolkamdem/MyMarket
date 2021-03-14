from django.shortcuts import render
from django.core.mail import send_mail
import yagmail

# Create your views here.

def home(request):
    send = False
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # send_mail(
        #     name,
        #     message,
        #     email,
        #     ['sagnolkamdem721@gmail.com']
        # )
        yag = yagmail.SMTP('sagnolkamdem721@gmail.com', 'sncyfredcdgapvvh')
        yag.send(to = email,
         subject = 'contact',
         contents = message)
        send = True
        return render(request, '../templates/base.html', locals())
        
    return render(request, '../templates/base.html')