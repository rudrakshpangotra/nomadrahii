
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_protect
from . models import hotels,shimla_customization,transport,price_of_basic_plan,users1,users1_customize,manali_customization,dalhousie_customization,dharamshala_customization,kinnaur_customization,spiti_customization
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from pathlib import Path
from django.contrib import messages
# Create your views here.
def index(request):
	return render(request,'hello/first.html')

def contact(request):
	return render(request,'hello/contact.html')

def signup(request):
	thank=False
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			thank=True
			username=form.cleaned_data.get('username')
			request.session['username']=username
			params={'thank':thank,'user':username}
			return render(request,'hello/first.html',params)
	else:
		form=UserCreationForm()
	return render(request,'registration/signup.html',{'form':form})
#@cache_control(no_cache=True,must_revalidate=True,no_store=True)
#@login_required(login_url='/login/')
def logout1(request):
	tyui=True
	request.session.flush()
	#logout(request)
	return render(request,'hello/first.html',{'tyui':tyui})
@csrf_protect
def login1(request):
	thank2=False
	thank3=False
	if(request.method=='POST'):
		username=request.POST.get('username')
		password=request.POST.get('password')
		user1=authenticate(username=username,password=password)
		if user1 is not None:
			if user1.is_active:
				login(request,user1)
				request.session['username']=username
				return redirect('/hello/')
			else:
				thank2=True
		else:
			thank3=True
			print(thank3)
			return render(request,'registration/login.html',{'thank3':thank3})
	return render(request,'registration/login.html',{'thank2':thank2,'thank3':thank3})

@login_required
def shimla(request):
	return render(request,'hello/shimla.html')
@login_required
def kinnaur(request):
	return render(request,'hello/kinnaur.html')
@login_required
def dalhousie(request):
	return render(request,'hello/dalhousie.html')
@login_required
def manali(request):
	return render(request,'hello/manali.html')
@login_required
def spiti(request):
	return render(request,'hello/spiti.html')
@login_required
def dharamshala(request):
	return render(request,'hello/dharamshala.html')

def booking(request,title,title1,title2):
	hotel1=hotels.objects.all().filter(hotel_location=title)
	transport1=transport.objects.all().filter(transport_location=title)
	prices=price_of_basic_plan.objects.all().filter(destination=title,no_of_days_plan=title1)
	thank=False
	if(request.method=="POST"):
		name=request.POST.get('name')
		email=request.POST.get('email')
		query=request.POST.get('destination')
		phone=request.POST.get('phone')
		members=request.POST.get('members')
		subject=request.POST.get('subject')
		plan=request.POST.get('subject4')
		start=request.POST.get('start')
		subject1=request.POST.get('hotels1')
		transport4=request.POST.get('transport')
		price=request.POST.get('price')
		contact1=users1(user_name=name,user_email=email,no_of_members=members,user_phone=phone,when_to_start=start,user_destination=query,user_plan=subject,user_plan_link=plan,user_hotel=subject1,price=price,user_transport=transport4)
		contact1.save()
		thank=True
		email_from=settings.EMAIL_HOST_USER
		subject=subject
		message=query
		recipient_list=['rudrakshpangotra2@gmail.com']
		send_mail(subject,message,email_from,recipient_list)
	return render(request,'hello/booking.html',{'title':title,'title1':title1,'title2':title2,'hotel':hotel1,'thank':thank,'transport1':transport1,'prices':prices[0]})

def customization(request,title):
	return render(request,'hello/customization.html',{'title':title})

def customize(request,title,number):
	thank=False
	thank1=False
	if(title=="Dalhousie"):
		shimla1=dalhousie_customization.objects.all().filter(no_of_days=1)
		shimla2=dalhousie_customization.objects.all().filter(no_of_days=2)
		shimla3=dalhousie_customization.objects.all().filter(no_of_days=3)
		shimla4=dalhousie_customization.objects.all().filter(no_of_days=4)
		shimla5=dalhousie_customization.objects.all().filter(no_of_days=5)
		shimla6=dalhousie_customization.objects.all().filter(no_of_days=6)
		shimla7=dalhousie_customization.objects.all().filter(no_of_days=7)
	
	if(title=="Manali"):
		shimla1=manali_customization.objects.all().filter(no_of_days=1)
		shimla2=manali_customization.objects.all().filter(no_of_days=2)
		shimla3=manali_customization.objects.all().filter(no_of_days=3)
		shimla4=manali_customization.objects.all().filter(no_of_days=4)
		shimla5=manali_customization.objects.all().filter(no_of_days=5)
		shimla6=manali_customization.objects.all().filter(no_of_days=6)
		shimla7=manali_customization.objects.all().filter(no_of_days=7)
	
	if(title=="Spiti"):
		shimla1=spiti_customization.objects.all().filter(no_of_days=1)
		shimla2=spiti_customization.objects.all().filter(no_of_days=2)
		shimla3=spiti_customization.objects.all().filter(no_of_days=3)
		shimla4=spiti_customization.objects.all().filter(no_of_days=4)
		shimla5=spiti_customization.objects.all().filter(no_of_days=5)
		shimla6=spiti_customization.objects.all().filter(no_of_days=6)
		shimla7=spiti_customization.objects.all().filter(no_of_days=7)
	
	if(title=="Kinnaur"):
		shimla1=kinnaur_customization.objects.all().filter(no_of_days=1)
		shimla2=kinnaur_customization.objects.all().filter(no_of_days=2)
		shimla3=kinnaur_customization.objects.all().filter(no_of_days=3)
		shimla4=kinnaur_customization.objects.all().filter(no_of_days=4)
		shimla5=kinnaur_customization.objects.all().filter(no_of_days=5)
		shimla6=kinnaur_customization.objects.all().filter(no_of_days=6)
		shimla7=kinnaur_customization.objects.all().filter(no_of_days=7)
	
	if(title=="Dharamshala"):
		shimla1=dharamshala_customization.objects.all().filter(no_of_days=1)
		shimla2=dharamshala_customization.objects.all().filter(no_of_days=2)
		shimla3=dharamshala_customization.objects.all().filter(no_of_days=3)
		shimla4=dharamshala_customization.objects.all().filter(no_of_days=4)
		shimla5=dharamshala_customization.objects.all().filter(no_of_days=5)
		shimla6=dharamshala_customization.objects.all().filter(no_of_days=6)
		shimla7=dharamshala_customization.objects.all().filter(no_of_days=7)
	
	if(title=="Shimla"):
		shimla1=shimla_customization.objects.all().filter(no_of_days=1)
		shimla2=shimla_customization.objects.all().filter(no_of_days=2)
		shimla3=shimla_customization.objects.all().filter(no_of_days=3)
		shimla4=shimla_customization.objects.all().filter(no_of_days=4)
		shimla5=shimla_customization.objects.all().filter(no_of_days=5)
		shimla6=shimla_customization.objects.all().filter(no_of_days=6)
		shimla7=shimla_customization.objects.all().filter(no_of_days=7)
	hotel1=hotels.objects.all().filter(hotel_location=title)
	transport1=transport.objects.all().filter(transport_location=title)
	if(request.method=="POST"):
		name=request.POST.get('name')
		email=request.POST.get('email')
		query=request.POST.get('destination')
		phone=request.POST.get('phone')
		member=request.POST.get('members')
		subject=request.POST.get('subject')
		when=request.POST.get('start')
		day1=request.POST.get('shimla1')
		day2=request.POST.get('shimla2')
		day3=request.POST.get('shimla3')
		day4=request.POST.get('shimla4')
		day5=request.POST.get('shimla5')
		day6=request.POST.get('shimla6')
		day7=request.POST.get('shimla7')
		if(day1!=""):
			total_plan="Day 1\n" + day1 +"\n"
		if(day2!=""):
			total_plan=total_plan + "Day 2\n" + day2 +"\n" 
		if(str(day3)!="None"):
		  	total_plan=total_plan + "Day 3\n" + day3 +"\n"
		if(str(day4)!="None"):
		  	total_plan=total_plan + "Day 4\n" + day4 +"\n" 
		if(str(day5)!="None"):
		  	total_plan=total_plan + "Day 5\n" + day5 +"\n"
		if(str(day6)!="None"):
		  	total_plan=total_plan + "Day 6\n" + day6 +"\n" 
		if(str(day7)!="None"):
		  	total_plan=total_plan+"Day 7\n" + day7 +"\n"
		total1=request.POST.get('total')
		subject1=request.POST.get('hotels1')
		transport4=request.POST.get('transport')
		price=request.POST.get('price')
		print(total1)
		if(subject1=="NULL" or transport4=="NULL" or price==0 or str(total1)=="None" or total1=="0" or total1==" "):
			thank1=True
		if(day1=="NULL" or day2=="NULL" or day3=="NULL" or day4=="NULL" or day5=="NULL" or day6=="NULL" or day7=="NULL"):
			thank1=True
		# Send Mail using template
		email_from=settings.EMAIL_HOST_USER
		to=[email_from, email]
		subject = 'Customized Plan for ' + query + ' has been booked by ' + name
		heading = 'Customized Plan for ' + query + ' has been booked by ' + name +' using email: ' + email
		text_content = 'Plan for '+ query + ' has been booked using email ' + email
		html_content = f"""<!doctype html>
    							<html lang=en>
        							<head>
            							<meta charset=utf-8>
            							<title>Nomad Raahi Booking</title>
        							</head>
        						<body>
            						<p>{heading}</p>
            						<br>
            						<p>
            						<img src="https://i.ibb.co/R29fsTj/logoprojectfinal.png" height="25%" width="25%" alt="Nomad Raahi Booking" border="0">
     								</p>
           
            						<p>
            						<strong>Username:</strong> {name}
            						<br>
            						<strong>Destination:</strong> {query}
            						<br>
            						<strong>Hotel:</strong> {subject1}
            						<br>
            						<strong>Customized Package:</strong> {subject}
            						</p>
        						</body>
    							</html>
						"""
		msg = EmailMultiAlternatives(subject, text_content, email_from, to)
		msg.attach_alternative(html_content, "text/html")
		if(thank1==False):
			msg.send()
			messages.success(request, 'Booking has been done ! Enjoy your trip')
		contact1=users1_customize(user_name=name,user_email=email,no_of_members=member,user_phone=phone,when_to_start=when,user_destination=query,user_plan=subject,user_plan_link=total_plan,user_hotel=subject1,price_other=price,user_transport=transport4,price_plan=total1)
		contact1.save()
	return render(request,'hello/customize.html',{'title':title,'number':number,'hotel':hotel1,'shimla1':shimla1,'shimla2':shimla2,'shimla3':shimla3,'shimla4':shimla4,'shimla5':shimla5,'shimla6':shimla6,'shimla7':shimla7,'transport1':transport1,'thank1':thank1,'thank':thank})

def previous_booking(request,name):
	user=users1.objects.all().filter(user_name=name)
	user1=users1_customize.objects.all().filter(user_name=name)
	return render(request,'hello/previous_booking.html',{'user':user,'user1':user1})





