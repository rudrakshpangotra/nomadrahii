from django.db import models

#Create your models here.

class price_of_basic_plan(models.Model):
	destination=models.CharField(max_length=100,default="")
	no_of_days_plan=models.CharField(max_length=100,default="")
	price=models.IntegerField(default=0)

class shimla_customization(models.Model):
	shimla_id=models.AutoField
	no_of_days=models.IntegerField(default=0)
	possibility=models.CharField(max_length=100,default="")
	price=models.IntegerField(default=0)

class dalhousie_customization(models.Model):
	dalhousie_id=models.AutoField
	no_of_days=models.IntegerField(default=0)
	possibility=models.CharField(max_length=100,default="")
	price=models.IntegerField(default=0)

class spiti_customization(models.Model):
	spiti_id=models.AutoField
	no_of_days=models.IntegerField(default=0)
	possibility=models.CharField(max_length=100,default="")
	price=models.IntegerField(default=0)

class kinnaur_customization(models.Model):
	kinnaur_id=models.AutoField
	no_of_days=models.IntegerField(default=0)
	possibility=models.CharField(max_length=100,default="")
	price=models.IntegerField(default=0)

class manali_customization(models.Model):
	manali_id=models.AutoField
	no_of_days=models.IntegerField(default=0)
	possibility=models.CharField(max_length=100,default="")
	price=models.IntegerField(default=0)

class dharamshala_customization(models.Model):
	dharamshala_id=models.AutoField
	no_of_days=models.IntegerField(default=0)
	possibility=models.CharField(max_length=100,default="")
	price=models.IntegerField(default=0)

class hotels(models.Model):
	hotel_id=models.IntegerField(primary_key=True,default=0)
	hotel_name=models.CharField(max_length=100,default="")
	hotel_location=models.CharField(max_length=100,default="")
	price=models.IntegerField(default=0)

class transport(models.Model):
	transport_id=models.IntegerField(primary_key=True,default=0)
	transport_name=models.CharField(max_length=100,default="")
	transport_location=models.CharField(max_length=100,default="")
	price=models.IntegerField(default=0)

class users1(models.Model):
	user_id=models.AutoField
	user_name=models.CharField(max_length=30,default="")
	user_email=models.CharField(max_length=20,default="")
	no_of_members=models.CharField(max_length=20,default="")
	user_phone=models.IntegerField(default=0)
	#start_date=models.DateField(null=True,blank=True)
	#start=models.CharField(max_length=10,default="")
	when_to_start=models.CharField(max_length=10,default="")
	user_destination=models.CharField(max_length=30,default="")
	user_plan=models.CharField(max_length=30,default="")
	user_plan_link=models.CharField(max_length=100,default="")
	user_hotel=models.CharField(max_length=30,default="")
	user_transport=models.CharField(max_length=30,default="")
	price=models.IntegerField(default=0)

class users1_customize(models.Model):
	user_id=models.AutoField
	user_name=models.CharField(max_length=30,default="")
	user_email=models.CharField(max_length=20,default="")
	no_of_members=models.CharField(max_length=20,default="")
	user_phone=models.IntegerField(default=0)
	#start_date=models.DateField(null=True,blank=True)
	#start=models.CharField(max_length=10,default="")
	when_to_start=models.CharField(max_length=10,default="")
	user_destination=models.CharField(max_length=30,default="")
	user_plan=models.CharField(max_length=30,default="")
	user_plan_link=models.CharField(max_length=100,default="")
	user_hotel=models.CharField(max_length=30,default="")
	user_transport=models.CharField(max_length=30,default="")
	price_plan=models.IntegerField(default=0)
	price_other=models.IntegerField(default=0)

