from django import forms
import datetime
from django.forms.widgets import DateInput

from .models import (
    School,
    AdmissionEnquiry, 
    AdmissionDetails, 
    Admission,
    Fees
)

def year_choices():
    return [(r,r) for r in range(1900, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year


class SchoolForm(forms.ModelForm):
    year_established = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
    class Meta:
        model = School
        fields = "__all__"
        
        
class AdmissionDetailsForm(forms.ModelForm):
    academic_year = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
    class Meta:
        model = AdmissionDetails
        exclude = ("school",)

class AdmissionEnquiryForm(forms.ModelForm):
    class Meta:
        model = AdmissionEnquiry
        fields = "__all__"


class FeesForm(forms.ModelForm):
    class Meta:
        model = Fees
        fields = "__all__"


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = "__all__"