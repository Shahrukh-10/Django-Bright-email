from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail 
from gmails.models import Userinfo
from django.db.models.functions import Trim
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        query = request.POST['query']
        info = Userinfo(name=name,email=email,query=query)
        
        res = send_mail(
            subject = f'New Query from {email}',
            message = f'''Name: {name}\nQuery: {query}''',
            from_email = 'Brightservicecentre1@gmail.com',
            recipient_list = ['test.testing.stark@gmail.com'],
            fail_silently=True,
        )  
        if res==1:
            messages.error(request,'Response sent successfully.')
            info.save()
            return render(request,'index.html')
        else:
            messages.error(request,'Some error occurred')
            return render(request,'index.html')
    return render(request,'index.html') 
