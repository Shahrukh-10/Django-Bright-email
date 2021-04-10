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
        info = Userinfo(name=Trim(name),email=Trim(email),query=Trim(query))
        
        res = send_mail(
            subject = 'Your query has been submitted',
            message = 'thanks for your feedback',
            from_email = 'Brightservicecentre1@gmail.com',
            recipient_list = [email],
            fail_silently=True,
        )  
        print(name,email,query,res)
        if res==1:
            messages.error(request,'Response sent successfully.')
            return render(request,'index.html')
        else:
            messages.error(request,'Some error occurred')
            return render(request,'index.html')
    return render(request,'index.html') 