from django.db import models
from django.utils import timezone
import datetime

from django.core.validators import MaxValueValidator, MinValueValidator


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

CLASSES_CHOICE = (
    ('Class Nursery', 'Class Nursery'),
    ('Class LKG', 'Class LKG'),
    ('Class PRE KG', 'Class PRE KG'),
    ('Class UKG', 'Class UKG'),
    ('Class I', 'Class I'),
    ('Class II', 'Class II'),
    ('Class III', 'Class III'),
    ('Class IV', 'Class IV'),
    ('Class V', 'Class V'),
    ('Class VI', 'Class VI'),
    ('Class VII', 'Class VII'),
    ('Class VIII', 'Class VIII'),
    ('Class IX', 'Class IX'),
    ('Class X', 'Class X'),
    ('Class XI', 'Class XI'),
    ('Class XII', 'Class XII'),
)

class School(models.Model):
    SCHOOL_CHOICE = (
        ("1","Public School"),
        ("2","Private School"),
        ("3","Trust"),
        ("4","Society"),
        ("5","Municipal School"),
        ("6","Government School"),
        ("7","State Government School"),
    )

    BOARDING_CHOICE = (
        ("1","Day school"),
        ("2","Day cum boarding school"),
        ("3","Play school"),
    )

    GENDER_CHOICE = (
        ("1","Coed"),
        ("2","Boys"),
        ("3","Girls"),
    )


    name = models.CharField(max_length=255, null=True)
    year_established = models.IntegerField(validators=[MinValueValidator(1900), max_value_current_year])
    email = models.EmailField(max_length=100, null=True, unique=True)
    phone_no = models.CharField(max_length=10, null=True, unique=True)
    chairman_name  = models.CharField(max_length=100, null=True)
    principal_name = models.CharField(max_length=100, null=True)
    school_type = models.CharField(choices= SCHOOL_CHOICE ,max_length=50, null=True)
    boarding = models.CharField(choices= BOARDING_CHOICE ,max_length=50, null=True)
    gender = models.CharField(choices= GENDER_CHOICE ,max_length=100, null=True)
    grades_start = models.CharField(choices= CLASSES_CHOICE ,max_length=50, null=True)
    grades_end = models.CharField(choices= CLASSES_CHOICE ,max_length=50, null=True)
    management = models.CharField(max_length=50, null=True)
    language_of_instruction = models.CharField(max_length=50, null=True)
    curriculum = models.CharField(max_length = 100, null=True)
    website = models.CharField(max_length = 255, blank=True, null=True)
    address = models.CharField(max_length=200,  null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name

class Fees(models.Model):
    
    FREQUENCY_CHOICE = (
        ("1","Monthly"),
        ("4","Quarterly"),
        ("6","Half yearly"),
        ("12","Annually"),
    )
    school = models.ForeignKey(to=School, on_delete=models.CASCADE, null=True)
    class_name = models.CharField(choices=CLASSES_CHOICE, max_length=100, null=True)
    fee_type = models.CharField(max_length=100, null=True)
    amount = models.IntegerField(default=0, null=True)
    frequency = models.CharField(choices=FREQUENCY_CHOICE, max_length=100, null=True)

    def __str__(self):
        return self.class_name


class Facilities(models.Model):

    school = models.ForeignKey(to=School, on_delete=models.CASCADE, null=True)
    sports_facilities = models.CharField(max_length=1000, null=True, blank=True)
    education_facilities = models.CharField(max_length=1000, null=True, blank=True)
    classroom_facilities = models.CharField(max_length=1000, null=True, blank=True)
    visual_and_performing_art_facilities = models.CharField(max_length=1000, null=True, blank=True)
    laboratories_facilities = models.CharField(max_length=1000, null=True, blank=True)
    transport_facilities = models.CharField(max_length=1000, null=True, blank=True)
    boarding_facilities = models.CharField(max_length=1000, null=True, blank=True)
    accessibility_facilities = models.CharField(max_length=1000, null=True, blank=True)
    digital_facilities = models.CharField(max_length=1000, null=True, blank=True)
    safety_and_security_facilities = models.CharField(max_length=1000, null=True, blank=True)
    food_and_catering_facilities = models.CharField(max_length=1000, null=True, blank=True)
    medical_facility_facilities = models.CharField(max_length=1000, null=True, blank=True)
    other_infra_facilities = models.CharField(max_length=1000, null=True, blank=True)



class AdmissionDetails(models.Model):
    school = models.ForeignKey(to=School, on_delete=models.CASCADE, null=True)
    academic_year = models.IntegerField(validators=[MinValueValidator(1984), max_value_current_year])
    admission_period = models.CharField(max_length=100, null=True)
    fee_details = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)



class Admission(models.Model):
    # school = models.ForeignKey(to=School, on_delete=models.CASCADE, null=True)
    class_name = models.CharField(choices=CLASSES_CHOICE, max_length=100, null=True)
    session = models.CharField(max_length=50,null=True)
    last_date = models.DateField(default=timezone.now,  null=True)
    application_fees = models.IntegerField(default=0, null=True)

 
class AdmissionEnquiry(models.Model):
    
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=255, null=True)
    phone = models.CharField(max_length=10, null=True)
    class_name = models.CharField(choices = CLASSES_CHOICE,max_length=20, null=True)
    message = models.TextField(max_length=200, null=True,blank=True)
