from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage


# Create your views here.




def page2(request):
    return render(request, "page2.html")


def data(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        email = request.POST['email']
        place = request.POST['place']

        template = get_template('details.txt')
        context = {'name': name, 'number': number, 'email': email, 'place': place}
        print(context)
        content = template.render(context)
        print(content)
        email = EmailMessage(
            "Contact form Recieved",
            content,
            "Contact Form" + '',
            ['envvumarketing3@gmail.com', 'envvumarketing6@gmail.com'],
            headers={'Reply To': email}
        )
        email.send()
        # messages.success(request, f'Thank You For Contacting Us , Our Executive Will Contact You Soon')
        # html = "<html><body><h2>Thank You For Contacting Us , Our Executive Will Contact You Soon</h2><br> <a href='https://www.newcristalacademy.com/'><h2>Home</h2></a> </body></html> "
        # return HttpResponse(html)
        return render(request, 'congratulation.html')

    return render(request, 'aa.html')


def page3(request):
    return render(request, 'page3.html')


def aa(request):
    return render(request, 'aa.html')

def congratulation(request):
    return render(request,'congratulation.html')