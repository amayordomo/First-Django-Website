from django.shortcuts import render
from .models import contact_list, contact_form
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print(f"Name: {name}, Email: {email}, Subject: {subject}, Message: {message}")

        contactformdata = contact_form(name=name, email=email, subject=subject, message=message)
        contactformdata.save()

    contactdata = contact_list.objects.all()[0]
    
    context = {
        'contactlist': contactdata,
    }

    return render(request, 'contact.html', context)

