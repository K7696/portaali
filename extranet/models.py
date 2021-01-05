from django.db import models

# Create your models here.
class CompanyCustomer(models.Model):
    # Id
    #id = models.AutoField(primary_key=True)

    # Y-tunnus
    business_identifier_code = models.CharField(max_length=20)
    # OVT
    organization_unit_number = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100)
    
    # Contact person
    contact_person_firstname = models.CharField(max_length=50)
    contact_person_lastname = models.CharField(max_length=50)
    contact_person_phonenumber = models.CharField(max_length=50)
    contact_person_email = models.CharField(max_length=50)
    
    # Address
    street_name = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    postal_address = models.CharField(max_length=100)
    
    # Dates
    created_datetime = models.DateTimeField('datetime created')
    modified_datetime = models.DateTimeField('datetime modified')
    
class PrivateCustomer(models.Model):
    # Id
    #id = models.AutoField(primary_key=True)

    # Contact person
    contact_person_firstname = models.CharField(max_length=50)
    contact_person_lastname = models.CharField(max_length=50)
    contact_person_phonenumber = models.CharField(max_length=50)
    contact_person_email = models.CharField(max_length=50)
    
    # Address
    street_name = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    postal_address = models.CharField(max_length=100)
    
    # Dates
    created_datetime = models.DateTimeField('datetime created')
    modified_datetime = models.DateTimeField('datetime modified')
    
    
    
    