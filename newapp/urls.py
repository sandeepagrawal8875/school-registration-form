from django.urls import path
from .views import (
    school,
    admissionDetails,
    admissionEnquiry,
    admission,
    home,
    facilities,
    fees
)

urlpatterns = [
    path('', home, name="home"),
    path('school', school, name="school"),
    path('facilities/<int:pk>', facilities, name="facilities"),
    path('Details', admissionDetails, name="Details"),
    path('Enquiry', admissionEnquiry, name="Enquiry"),
    path('admission', admission, name="admission"),
    path('fees', fees, name="fees"),
]