from django.db import models
from .validators import*
class ContactInfo(models.Model):
    mobile_number = models.CharField(max_length=15,validators=[validate_mobile_no])
    phone_number = models.CharField(max_length=15,validators=[validate_phone_no])
    email_id = models.EmailField()
class Address(models.Model):
    address_id= models.AutoField(primary_key=True)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=10)
    city = models.CharField(max_length=20,validators=[validate_city])
    state= models.CharField(max_length=20,validators=[validate_state])
    landmark= models.CharField(max_length=20,validators=[validate_landmark])
    pincode= models.IntegerField()
class AgentReferals(models.Model):
    referal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,validators=[validate_name])
    verified = models.BinaryField(default=True)
class Media(models.Model):
    media_id =models.AutoField(primary_key=True)
    media_name= models.CharField(max_length=50,validators=[validate_media_name])
    media_path= models.FileField(upload_to='documents/')
class Location(models.Model):
    loc_name = models.CharField(max_length=20,validators=[validate_loc_name])
class PropertyType(models.Model):
    property_type_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
class Agent(ContactInfo,Media):
    agent_id= models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=20,validators=[validate_first_name])
    last_name= models.CharField(max_length=20,validators=[validate_last_name])
    age=models.IntegerField()
    education= models.CharField(max_length=50,validators=[validate_education])
    company_name=models.CharField(max_length=50)
    specialization= models.CharField(max_length=100,validators=[validate_specelization])
    experence=models.IntegerField()
    agent_notes=models.TextField()
    address = models.ManyToManyField("Address")
    agentreferal = models.ManyToManyField("AgentReferals")
    location = models.ManyToManyField("Location")
    propertytype = models.ManyToManyField("PropertyType")
