from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail,BadHeaderError
from django.conf import settings
# Create your views here.
def contact_page(req):
    form = ContactForm(req.POST or None)
    if req.method=='POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            msg = form.cleaned_data.get('msg')
            print(name,email,msg)
            try:
                send_mail(name,msg,email,['aliceprerna@gmail.com'],fail_silently=False,)
            except BadHeaderError:
                return HttpResponse('Invalid Header found!')
            else:
                return HttpResponse('<h1>Success</h1>')

    return render(req,'contact/contact_page.html',{'form':form})
